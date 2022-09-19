from PIL import Image
import numpy as np
import logging as log
import time
log.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    level=log.ERROR
)
def removeDuplicates(array):
    newArr = []
    for i in array:
        if i not in newArr:
            newArr.append(i)
    return newArr
def printMat(mat):
	for m in mat:
		print(m)
def readRGB(filename,resize=False):
    size = 16,16
    img = Image.open(filename)
    if resize:
        img = img.resize(size,Image.Resampling.LANCZOS)
        img= img.convert('RGB')
    numpydata = np.asarray(img)
    R=[]
    G=[]
    B=[]
    A=[]
    for row in numpydata:
        for pixel in row:
            R.append(pixel[0])
            G.append(pixel[1])
            B.append(pixel[2])
            if not resize:
                A.append(pixel[3])
    return (R,G,B,A,img.size)
def encryptDecryptPixel(encryptResult,i,halfLength,colorKeyMatrix,color,isEncryption=True):
    floc = findLoc(colorKeyMatrix,color[i])
    sloc = findLoc(colorKeyMatrix,color[halfLength+i])
    if isEncryption:
        floc[0]=(floc[0]+9)%16
        floc[1]=(floc[1]+9)%16
        sloc[0]=(sloc[0]+9)%16
        sloc[1]=(sloc[1]+9)%16
        if floc[0] == sloc[0]:
            encryptResult[i]=colorKeyMatrix[floc[0],(floc[1]+1)%16]
            encryptResult[halfLength+i] = colorKeyMatrix[sloc[0],(sloc[1]+1)%16]
        elif floc[1] == sloc[1]:
            encryptResult[i]=colorKeyMatrix[(floc[0]+1)%16,floc[1]]
            encryptResult[halfLength+i] = colorKeyMatrix[(sloc[0]+1)%16,sloc[1]]
        else:
            encryptResult[i]=colorKeyMatrix[floc[0],sloc[1]]
            encryptResult[halfLength+i] = colorKeyMatrix[sloc[0],floc[1]]
    else:  
        floc[0]=(floc[0]+7)%16
        floc[1]=(floc[1]+7)%16
        sloc[0]=(sloc[0]+7)%16
        sloc[1]=(sloc[1]+7)%16
        if floc[0] == sloc[0]:
            encryptResult[i]=colorKeyMatrix[floc[0],(floc[1]+15)%16]
            encryptResult[halfLength+i] = colorKeyMatrix[sloc[0],(sloc[1]+15)%16]
        elif floc[1] == sloc[1]:
            encryptResult[i]=colorKeyMatrix[(floc[0]+15)%16,floc[1]]
            encryptResult[halfLength+i] = colorKeyMatrix[(sloc[0]+15)%16,sloc[1]]
        else:
            encryptResult[i]=colorKeyMatrix[floc[0],sloc[1]]
            encryptResult[halfLength+i] = colorKeyMatrix[sloc[0],floc[1]]
R,G,B,A,s=readRGB('key.png',True)
R=removeDuplicates(R)
G=removeDuplicates(G)
B=removeDuplicates(B)
R.extend([x for x in range(256) if x not in R])
RkeyMatrix = np.reshape(R, (16,16))
G.extend([x for x in range(256) if x not in G])
GkeyMatrix = np.reshape(G, (16,16))
B.extend([x for x in range(256) if x not in B])
BkeyMatrix = np.reshape(B, (16,16))
log.debug('R key matrix:')
log.debug(RkeyMatrix)
log.debug('G key matrix:')
log.debug(GkeyMatrix)
log.debug('B key matrix:')
log.debug(BkeyMatrix)

def findLoc(mat,x):
    coordinates = np.where(mat==x)
    return [coordinates[0][0],coordinates[1][0]]
def encrypt():
    #inp = input("Enter image file name to encrypt= ")
    #R,G,B=readRGB(inp,False)
    R,G,B,A,sizes=readRGB('RSCN10331.png',False)
    log.info(sizes)
    encryptedR=np.full(len(R),-1)
    encryptedG=np.full(len(G),-1)
    encryptedB=np.full(len(B),-1)
    log.info(encryptedR.shape)
    halfLength = len(R)//2
    for i in range(halfLength):
       encryptDecryptPixel(encryptedR,i,halfLength,BkeyMatrix,R)
       encryptDecryptPixel(encryptedG,i,halfLength,RkeyMatrix,G)
       encryptDecryptPixel(encryptedB,i,halfLength,GkeyMatrix,B)
    fullImage1D=[]
    log.debug(f'encryption {R=}')
    log.debug(f'{encryptedR=}')
    log.debug(f'encryption {G=}')
    log.debug(f'encryption {B=}')
    log.debug(f'encryption {A=}')
    for i in range(len(encryptedR)):
        fullImage1D.append([encryptedR[i],encryptedG[i],encryptedB[i],A[i]])
    # print(fullImage1D)
    x,y,z=sizes[0],sizes[1],4
    imageArr = np.reshape(fullImage1D,(y,x,z))
    # print(f'{imageArr=}')
    image = Image.fromarray(imageArr.astype('uint8'),'RGBA')
    # print(np.asarray(image))
    image.save('enc.png')

def decrypt():
    #inp = input("Enter image file name to encrypt= ")
    #R,G,B=readRGB(inp,False)
    R,G,B,A,sizes=readRGB('enc.png',False)
    decryptedR=np.full(len(R),-1)
    decryptedG=np.full(len(G),-1)
    decryptedB=np.full(len(B),-1)
    halfLength = len(R)//2
    for i in range(halfLength):
        encryptDecryptPixel(decryptedR,i,halfLength,BkeyMatrix,R,False)
        encryptDecryptPixel(decryptedG,i,halfLength,RkeyMatrix,G,False)
        encryptDecryptPixel(decryptedB,i,halfLength,GkeyMatrix,B,False)
    fullImage1D=[]
    log.debug(f'decryption {R=}')
    log.debug(f'{decryptedR=}')
    log.debug(f'decryption {G=}')
    log.debug(f'decryption {B=}')
    log.debug(f'decryption {A=}')
    for i in range(len(decryptedR)):
        fullImage1D.append([decryptedR[i],decryptedG[i],decryptedB[i],A[i]])
    # print("fullImage1D:",len(fullImage1D))
    x,y,z=sizes[0],sizes[1],4
    imageArr = np.reshape(fullImage1D,(y,x,z))
    image = Image.fromarray(imageArr.astype('uint8'),'RGBA')
    image.save('original.png')
encrypt()
time.sleep(2)
decrypt()