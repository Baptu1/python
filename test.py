
from sys import argv
#WAP to print sum and sub of given by cmd line arguments..: 
y=argv[1:]
sub=0
sum=0
for x in y:
    
    if(int(x)>sub):
        sub = int(x) - sub
    else:
        sub=sub - int(x)
    sum=int(x)+sum
print('The sum:',sum)
print('The sub:',sub)