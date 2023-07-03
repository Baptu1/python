n=int(input('enter any number:'))
if n<=1:
    print('the number{} is not prime'.format(n))
else:
    #is_prime=True
    for i in range(2,n//2+1):
        if n%i==0:
            print('the number {} is not prime'.format(n))
            #is_prime=False
            break
    #if is_prime==True:
       # print('the number {} is not prime'.format(n))
    else:
        print('the number {} is prime'.format(n))