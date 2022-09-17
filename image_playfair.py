from PIL import Image
import numpy as np
import logging as log
import time
log.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    level=log.INFO
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
log.info('R key matrix:')
print(RkeyMatrix)
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
    R,G,B,A,sizes=readRGB('toBeEncrypted.png',False)
    log.info(sizes)
    encryptedR=np.full(len(R),-1)
    log.info(encryptedR.shape)
    halfLength = len(R)//2
    for i in range(halfLength):
        floc = findLoc(RkeyMatrix,R[i])
        sloc = findLoc(RkeyMatrix,R[halfLength+i])
        if floc[0] == sloc[0]:
            encryptedR[i]=RkeyMatrix[floc[0],(floc[1]+1)%16]
            encryptedR[halfLength+i] = RkeyMatrix[sloc[0],(sloc[1]+1)%16]
        elif floc[1] == sloc[1]:
            encryptedR[i]=RkeyMatrix[(floc[0]+1)%16,floc[1]]
            encryptedR[halfLength+i] = RkeyMatrix[(sloc[0]+1)%16,sloc[1]]
        else:
            encryptedR[i]=RkeyMatrix[floc[0],sloc[1]]
            encryptedR[halfLength+i] = RkeyMatrix[sloc[0],floc[1]]
    fullImage1D=[]
    print(f'encryption {R=}')
    print(f'{encryptedR=}')
    print(f'encryption {G=}')
    print(f'encryption {B=}')
    print(f'encryption {A=}')
    for i in range(len(encryptedR)):
        fullImage1D.append([encryptedR[i],G[i],B[i],A[i]])
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
    halfLength = len(R)//2
    for i in range(halfLength):
        # print(i)
        floc = findLoc(RkeyMatrix,R[i])
        sloc = findLoc(RkeyMatrix,R[halfLength+i])
        if floc[0] == sloc[0]:
            decryptedR[i]=RkeyMatrix[floc[0],(floc[1]+15)%16]
            decryptedR[halfLength+i] = RkeyMatrix[sloc[0],(sloc[1]+15)%16]
        elif floc[1] == sloc[1]:
            decryptedR[i]=RkeyMatrix[(floc[0]+15)%16,floc[1]]
            decryptedR[halfLength+i] = RkeyMatrix[(sloc[0]+15)%16,sloc[1]]
        else:
            decryptedR[i]=RkeyMatrix[floc[0],sloc[1]]
            decryptedR[halfLength+i] = RkeyMatrix[sloc[0],floc[1]]
    fullImage1D=[]
    print(f'decryption {R=}')
    print(f'{decryptedR=}')
    print(f'decryption {G=}')
    print(f'decryption {B=}')
    print(f'decryption {A=}')
    for i in range(len(decryptedR)):
        fullImage1D.append([decryptedR[i],G[i],B[i],A[i]])
    # print("fullImage1D:",len(fullImage1D))
    x,y,z=sizes[0],sizes[1],4
    imageArr = np.reshape(fullImage1D,(y,x,z))
    image = Image.fromarray(imageArr.astype('uint8'),'RGBA')
    image.save('original.png')
    time.sleep(2)
    R,G,B,A,s=readRGB('original.png')
    print(f'decryption {R=}')
    print(f'decryption {G=}')
    print(f'decryption {B=}')
encrypt()
time.sleep(2)
decrypt()