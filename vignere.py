key = input("Enter Key [A-Z] = ")
key = key.upper()
key = key.replace(" ", "")

def encrypt():
	inp = input("Enter text to encrypt= ")
	inp = inp.upper()
	inp = inp.replace(" ", "")
	key1 = ''
	for i in range(0,len(inp)):
		key1 = key1+key[i%len(key)]
	
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