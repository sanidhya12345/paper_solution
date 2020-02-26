x=input()
p=''
for i in x:
    if ord(i)>=65 and ord(i)<=90:
        p=ord(i)+32
    if ord(i)>=97 and ord(i)<=122:
        p=ord(i)-32
    print(chr(p),end="")
