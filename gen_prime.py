n=int(input('enter a number:'))
n1=2 #2 is a first prime number
while n1<=n:
    #this code to check n1 is prime;
    #is_prime=True
    for i in range(2,n1):
        if n1%i==0:
            #is_prime=False
            continue
        print(n1) 
    n1=n1+1
    #if is_prime==True:
           # print(n1)
    #n1=n1+1


