n=int(input('enter a number:'))
for i in range(n):
    print(' '*(n-1-i)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-1-i))
#i=i+1