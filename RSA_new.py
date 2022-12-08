import math
pt=10
p=11
q=17
n=p*q
print(n)
phi=(p-1)*(q-1)
print(phi)
for i in range(2,phi):
    if(math.gcd(i,phi)==1):
        e=i
        break
e=7
print('Public key E=',e)
ct=pow(pt,e)%n
ct = int(ct)
print('Cipher text is: ',ct)
for i in range(2,phi):
    if((i*e)%phi==1):
        d=i
print("Private key is: ",d)
dt = pow(ct,d)%n
print("Decrypted Text: ",dt)