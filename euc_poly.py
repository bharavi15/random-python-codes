import numpy as np


def polymoddivision(x,y):
    quotient = 0
    y_len = y.bit_length()
    while True:
        shift = x.bit_length() - y_len
        if shift < 0:
            return (quotient , x)
        quotient = quotient ^ (1 << shift)
        x = x ^ (y << shift)

def polymodinverse(a, mod):
    r, x, y = polygcd(a, mod)
    if r == 1:
        return x

def polygcd(x,y):
    x = (x, 1, 0)
    y = (y, 0, 1)
    while True:
        q, r = polymoddivision(x[0], y[0])
        if not r:
            return y
        x , y = y , (r, x[1] ^ polymultiply(q, y[1]), x[2] ^ polymultiply(q, y[2]))

def polymultiply(x, y):
    product = 0
    while x and y:
        if x & 1: 
            product = product ^ y
        x >>= 1
        y <<= 1
    return product


def multplicativeInverse(polyA, polyB):
    n1 = polymodinverse(polyA, polyB)
    n1 = bin(n1)[2:]
    n2 = polymodinverse(polyB, polyA)
    n2 = bin(n2)[2:]
    bit_word1 = []
    bit_word2 = []
    poly11 = []
    poly22 = []
    for k in n1:
        bit_word1.append(int(k))
    for l in n2:
        bit_word2.append(int(l))
    for k in bin(polyA)[2:]:
        poly11.append(int(k))
    for l in bin(polyB)[2:]:
        poly22.append(int(l))
    polynom1 = np.poly1d(bit_word1)
    polynom2 = np.poly1d(bit_word2)

    print('The multplicative inverses of: ')
    print(np.poly1d(poly11), 'is:')
    print(polynom1)
    print('================================')
    print(bit_word1)
    print('================================')
    return bit_word1
    # print(np.poly1d(poly22), 'is:')
    # print(polynom2)

if __name__ == '__main__':
    polyA = 0b1011
    polyB = 0b10011
    print(multplicativeInverse(polyA, polyB))