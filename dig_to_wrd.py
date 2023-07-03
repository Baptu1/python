words_upto_19=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
words_of_tens=['','','twenty','thirty','fortey','fifty','sixty','seventy','eighty','ninety']
words_of_hundreds=['','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
n=int(input('enter any number between 0 to 999:'))
#print=''
d1=(n%100)
if n==0:
    print('zero')
elif n<=19:
    print(words_upto_19[n])
elif n<=99:
    print(words_of_tens[n//10]+' '+words_upto_19[n%10])
elif n<=999 and d1<=19:
    print(words_of_hundreds[n//100]+' '+words_upto_19[d1])
elif n<=999:
   print(words_of_hundreds[n//100]+' '+words_of_tens[d1//10]+' '+words_upto_19[d1%10])
else:
    print('please enter a number between 0 to 999')
