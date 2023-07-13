n=int(input('enter a number:'))
#wap to print '*' n number of time..
for i in range(n):
    print('*')
print('-'*30)
#wap to print '*' n number of time in a line...
for i in range(n):
    print('* ',end='')
print()   
print('-'*30)
#wap to print squre with '*'..
for i in range(n):
    print('* '*n)
print('-'*30)
#wap to print squre with digit in evry row..
for i in range(n):
    print((str(i+1)+' ')*n)
print('-'*30)
#wap to print squre with alphabets...
for i in range(n):
    print((chr(64+i+1)+' ')*n) #chr(65)=A,chr(66)=B
print('-'*30)
#wap to print right angle triangle..
a=1
for i in range(n):
    print((i+1)*'* ')
print('-'*30)    
#wap to print inverted right triangle..
for i in range(n):
    print('* '*(n-i))
print('-'*30)
#wap to print pyramid with '*'..
for i in range (n):
    print(' '*(n-i-1)+'* '*(i+1))
print('-'*30)
#wap to print inverted pyramid with '*'..
for i in range(n):
    print(' '*i+'* '*(n-i))
print('-'*30)
#wap to print diamond pattern with '*'..
for i in range (n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range (n):
        print(' '*(i+1)+'* '*(n-i-1))