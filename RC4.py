key=input("Enter key:")
s=[n for n in range(0,256)]
t=[]
for i in range(256):
    t.append(key[i%len(key)])
j=0
for i in range(0,256):
    j=(j+s[i]+ord(t[i]))%256
    s[i],s[j]=s[j],s[i]
pt=input("Enter PlainText:")
z,ct=[],[]
for l in range(0,len(pt)):
    i=(l+1)%256
    j=(s[i]+j)%256
    z.append(s[(s[i]+s[j])%256])
    ct.append(chr(ord(pt[l])^z[l]))
print("Encrypted text:"+''.join(ct))
newpt=[]
for l in range(0,len(ct)):
    newpt.append(chr(ord(ct[l])^z[l]))
print("Decrypted text:"+''.join(newpt))