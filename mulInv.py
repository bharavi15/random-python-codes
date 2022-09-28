# Multiplicative Inverse Using Extended Euclidean Algorithm
quotients = []
# Getting the GCD of the two numbers
def gcd(m,n):
    if m<n:
        n,m=m,n
    quotients.append(m//n)
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
[a,b] = [int(x) for x in input("Enter two numbers separated by spaces: ").split()]
gcdVal = gcd(a,b)
if gcdVal != 1:
    print('Multiplicative Inverse does not exist as GCD is not 1')
    exit()
quotients = quotients[:-1]
mat = [[1,0],[0,1]]
for i in quotients:
    l=mat[1][:]
    mat[1] = [mat[1][0]*i,mat[1][1]*i]
    mat[1] = [mat[0][0]-mat[1][0],mat[0][1]-mat[1][1]]
    mat[0] = l
print(f'Multiplicative Inverse of {a} mod {b} is {mat[1][0]}')
print(f'Multiplicative Inverse of {b} mod {a} is {mat[1][1]}')