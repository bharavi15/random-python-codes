key = input("Enter Key [A-Z 0-9] = ")
key = key.upper()
key = key.replace(" ", "")
keysList = []
for k in key:
	if k not in keysList:
		keysList.append(k)
def printMat(mat):
	for m in mat:
		print(m)
def printEmptyMat():
	for i in range(6):
		for j in range(6):
			print(f'({i},{j})',end=' ')
		print()
mat = [[-1 for i in range(0,6)] for j in range(0,6)]
i,j=0,0
for k in keysList:
	mat[i][j]=k
	j=(j+1)%6
	if j == 0:
		i=i+1
for k in range(48,58):
	if chr(k) not in keysList:
		mat[i][j]=chr(k)
		j=(j+1)%6
		if j == 0:
			i=i+1
for k in range(65,91):
	if chr(k) not in keysList:
		mat[i][j]=chr(k)
		j=(j+1)%6
		if j == 0:
			i=i+1
printMat(mat)
#printEmptyMat()
def encrypt():
	inp = input("Enter text to encrypt= ")
	inp = inp.upper()
	inp = inp.replace(" ", "")
	finalInp=''
	for i in range(0,len(inp)-1,2):
		if inp[i] == inp[i+1]:
			finalInp+=inp[i]+'X'+inp[i+1]
		else:
			finalInp+=inp[i]+inp[i+1]
	print(finalInp)
	if len(inp)%2 != 0:
		inp=inp+'X'
	cipherText = ''
	for i in range(0,len(inp),2):
		pt=inp[i:i+2]
		floc = findLoc(pt[0])
		sloc = findLoc(pt[1])
		if floc[0] is sloc[0]:
			cipherText=cipherText+mat[floc[0]][(floc[1]+1)%6]+mat[sloc[0]][(sloc[1]+1)%6]
		elif floc[1] is sloc[1]:
			cipherText=cipherText+mat[(floc[0]+1)%6][floc[1]]+mat[(sloc[0]+1)%6][sloc[1]]
		else:
			cipherText=cipherText+mat[floc[0]][sloc[1]]+mat[sloc[0]][floc[1]]
	print(f'cipherText= {cipherText}')
def decrypt():
	inp = input("Enter text to decrypt= ")
	inp = inp.upper()
	inp = inp.replace(" ", "")
	plainText = ''
	for i in range(0,len(inp),2):
		pt=inp[i:i+2]
		floc = findLoc(pt[0])
		sloc = findLoc(pt[1])
		if floc[0] is sloc[0]:
			plainText=plainText+mat[floc[0]][(floc[1]+5)%6]+mat[sloc[0]][(sloc[1]+5)%6]
		elif floc[1] is sloc[1]:
			plainText=plainText+mat[(floc[0]+5)%6][floc[1]]+mat[(sloc[0]+5)%6][sloc[1]]
		else:
			plainText=plainText+mat[floc[0]][sloc[1]]+mat[sloc[0]][floc[1]]
	print(f'plaintext= {plainText}')
def findLoc(ch):
	x,y=-1,-1
	for i in range(6):
		try:
			y=mat[i].index(ch)
			break
		except ValueError:
			pass
	for i in range(6):
		try:
			x=[row[i] for row in mat].index(ch)
			break
		except ValueError:
			pass
	#print(f"found {ch} at ({x+1},{y+1})")
	return [x,y]
while(1):
	inp = int(input("1. Encrypt \n2. Decrypt \n3. Exit\nEnter your choice="))
	if inp ==1 :
		encrypt()
	elif inp == 2:
		decrypt()
	elif inp == 3:
		exit()
	else:
		print("Enter correct option!")