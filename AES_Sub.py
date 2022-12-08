from euc_poly import multiplicativeInverse

polyA = 0x55
aesPrimitive = 0x11B
inv = multiplicativeInverse(polyA, aesPrimitive)
print(inv)
if len(inv) < 8:
    for i in range(8-len(inv)):
        inv.insert(0,0)
print(inv)
constMatMul = [[1,0,0,0,1,1,1,1],[1,1,0,0,0,1,1,1],[1,1,1,0,0,0,1,1],[1,1,1,1,0,0,0,1],[1,1,1,1,1,0,0,0],[0,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0],[0,0,0,1,1,1,1,1]]
mul=[]
for i in range(8):
    s=0
    k=7
    for j in range(8):
        s^=constMatMul[i][j]&inv[k]
        k-=1
    mul.append(s)
print(mul)
s=[]
constant2 = [1,1,0,0,0,1,1,0]
for i in range(8):
    s.append(constant2[i]^mul[i])
res = list(reversed(s))
s1 = [str(res[i]) for i in range(len(res))]

print( hex(int(''.join(s1),2)))
