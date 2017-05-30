sum = 0
S='SPAM'
L=[]
for i in S:
    print(ord(i), end=' ')
    sum+=ord(i)
    L.append(ord(i))
print()
print('the sum of ascii codes in',S,'is',sum)
print(L)

