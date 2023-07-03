#wap to print first n numbers of 3's factor:
n=int(input('enter n value:'))
count=0
n1=3
while True:
    #for i in range(3,):
    if n1%3==0:
            print(n1)
            count=count+1
            #break
    if count==n:
        break
    n1=n1+1