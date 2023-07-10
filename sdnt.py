#WAP student management application..
n=int(input('enter number of student:'))
d={}
for i in range(n):
    student=input('Enter Student name:')
    marks=int(input('Enter sutdent marks:'))
    d[student]=marks
print('student data submitted complete..')
print('#'*30)
print('STUDENT','\t','MARKS')
for k,v in d.items():
    print(k,'\t\t',v)
print('#'*30)  
print('search operation started..')  
while True:
    name=input('enter student name:')
    marks=d.get(name,-1)
    if marks==-1:
        print(name,'not in the list')
    else:
        print('marks of',name ,'is',marks)
        option=input('do you want to find another student marks(YES/NO):')
        if option.upper()=='NO':
            break
print('thanks for using my application')
