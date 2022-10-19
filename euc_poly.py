import numpy as np
def polymultiply(x, y):
    result = 0
    while x and y:
        if x & 1: 
            result = result ^ y
        x >>= 1
        y <<= 1
    return result

def polymoddivision(x,y):
    q = 0
    ylen = y.bit_length()
    while True:
        shift = x.bit_length() - ylen
        if shift < 0:
            return (q , x)
        q = q ^ (1 << shift)
        x = x ^ (y << shift)

def polygcd(x,y):
    x = (x, 1, 0)
    y = (y, 0, 1)
    while True:
        q, r = polymoddivision(x[0], y[0])
        if not r:
            return y
        x , y = y , (r, x[1] ^ polymultiply(q, y[1]), x[2] ^ polymultiply(q, y[2]))

def polymodinverse(a, mod):
    r, x, y = polygcd(a, mod)
    if r == 1:
        return x

poly1 = 0b1100
poly2 = 0b100011011
n1 = polymodinverse(poly1, poly2)
n1 = bin(n1)[2:]
n2 = polymodinverse(poly2, poly1)
n2 = bin(n2)[2:]
bit_word1 = []
bit_word2 = []
poly11 = []
poly22 = []
for k in n1:
    bit_word1.append(int(k))
for l in n2:
    bit_word2.append(int(l))
for k in bin(poly1)[2:]:
    poly11.append(int(k))
for l in bin(poly2)[2:]:
    poly22.append(int(l))
polynom1 = np.poly1d(bit_word1)
polynom2 = np.poly1d(bit_word2)

print('The multplicative inverses of: ')
print()
print(np.poly1d(poly11), 'is:')
print(polynom1)
print()
print(np.poly1d(poly22), 'is:')
print(polynom2)