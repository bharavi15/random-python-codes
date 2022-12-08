import time
def lfsr(l,tapBits):
    op=l[0]
    s=0
    for i in range(len(tapBits)):
        s^=l[tapBits[i]]
    l.append(s)
    l.pop(0)
    return (op,l)
def searchList(l,item):
    retList = []
    for i in range(len(l)):
        if l[i]==item:
            retList.append(i)
    return retList

l1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
l2 = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# l1=[int(x) for x in input("Enter the First Polynomial")]
# l2=[int(x) for x in input("Enter the Second Polynomial")]
l1TapBits = searchList(l1,1)
l2TapBits = searchList(l2,1)
print('Tap Bits for l1=',l1TapBits)
print('Tap Bits for l2=',l2TapBits)
a=time.time()
with open('a5Op.txt', 'w') as f:
    s=''
    for i in range(1,10000001):
        op1,l1 = lfsr(l1,l1TapBits)
        op2,l2 = lfsr(l2,l2TapBits)
        s+=str(op1^op2)
        if(i%1000==0):
            f.write(s)
            s=''
print('end time:',time.time()-a)