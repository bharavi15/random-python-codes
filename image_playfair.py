from PIL import Image
from numpy import asarray
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
numpydata = asarray(img)
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
RkeyMatrix = [[-1 for i in range(16)] for j in range(16)]
GkeyMatrix = [[-1 for i in range(16)] for j in range(16)]
BkeyMatrix = [[-1 for i in range(16)] for j in range(16)]
i,j=0,0
for k in R:
    RkeyMatrix[i][j]=k
    j=(j+1)%16
    if j == 0:
        i=i+1
for k in range(256):
    if k not in R:
        RkeyMatrix[i][j]=k
        j=(j+1)%16
        if j == 0:
            i=i+1
printMat(RkeyMatrix)

i,j=0,0
for k in G:
    GkeyMatrix[i][j]=k
    j=(j+1)%16
    if j == 0:
        i=i+1
for k in range(256):
    if k not in G:
        GkeyMatrix[i][j]=k
        j=(j+1)%16
        if j == 0:
            i=i+1
printMat(GkeyMatrix)

i,j=0,0
for k in B:
    BkeyMatrix[i][j]=k
    j=(j+1)%16
    if j == 0:
        i=i+1
for k in range(256):
    if k not in B:
        BkeyMatrix[i][j]=k
        j=(j+1)%16
        if j == 0:
            i=i+1
printMat(BkeyMatrix)
