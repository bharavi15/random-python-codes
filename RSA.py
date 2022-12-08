import math
m=80
p=11
q=13
n=p*q
d=0
print(n)
phi=(p-1)*(q-1)
print(phi)

for i in range(1,phi):
    if(math.gcd(i,phi)==1):
        e=i

print('Public key E=',e)
ct=math.pow(m,e)%n
print('Cipher text is: ',ct)    

# n=99
# e=2
# phi=80
for k in range(1,n):
    x=((k*phi)+1)/e
    (x,rem)=divmod(((k*phi)+1),e)
    print((x,rem))
    if(rem==0):
        d=x
        break
print('private key D=',d)

pt=math.pow(ct,d)%n
print('Plain text is: ',pt)