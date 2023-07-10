word=input('enter any word:')
Vowels=['a','e','i','o','u']
d={}
for ch in word:
    if ch in Vowels:
        d[ch]=d.get(ch,0)+1
for k,v in d.items():
    print(k,'occur',v,'times')