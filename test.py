from sys import argv
y=argv[1:]
sub=0
for x in y:
    if(int(x)>sub):
        sub = int(x) - sub
    else:
        sub=sub - int(x)
print('The sub:',sub)