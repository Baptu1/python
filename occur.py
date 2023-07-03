s=input('enter string:')
subs=input('enter substring:')
i=s.find(subs)
if i==-1:
    print('substring is not available')
c=0 #counting the occurence
while i!=-1:
    c=c+1
    print('{} present at index:{}'.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))
print('the number of occurrancess:',c)