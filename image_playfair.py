from PIL import Image
import numpy as np
def removeDuplicates(array):
    newArr = []
    for i in array:
        if i not in newArr:
            newArr.append(i)
    return newArr
def printMat(mat):
	for m in mat:
		print(m)
size = 16,16
img = Image.open('Untitled1.png')
img = img.resize(size,Image.Resampling.LANCZOS)
numpydata = np.asarray(img)
# print(numpydata)
R=[]
G=[]
B=[]
for row in numpydata:
    for pixel in row:
        R.append(pixel[0])
        G.append(pixel[1])
        B.append(pixel[2])
# print(R)
# print(removeDuplicates(R))
R=removeDuplicates(R)
G=removeDuplicates(G)
B=removeDuplicates(B)
R.extend([x for x in range(256) if x not in R])
RkeyMatrix = np.reshape(R, (16,16))
G.extend([x for x in range(256) if x not in G])
GkeyMatrix = np.reshape(G, (16,16))
B.extend([x for x in range(256) if x not in B])
BkeyMatrix = np.reshape(B, (16,16))
print('R key matrix:\n', RkeyMatrix, '\nG key matrix:\n', GkeyMatrix, '\nB key matrix:\n', BkeyMatrix)
