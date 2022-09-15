from re import split
str="Test_Is*Over_For#This_Week"
pattern = r"[^a-zA-z]|_"
chars = list(reversed([x for x in str if not ((ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=123))]))
# print(f'{chars=}')
lst = split(pattern,str)
# print(f'{lst=}')
j=0
for i in list(reversed(lst)):
    c=''
    try:
        c=chars[j]
    except IndexError:
        c=''
    print(f'{i}{c}',end='')
    j+=1