#entr any string from keyword and print +ve and -ve index of each characters of the string...
s=input('enter some string:')
i=0
for x in s:
    print('the character present at +ve index:{} and -ve index:{} is:{}'.format(i,i-len(s),x))
    i=i+1