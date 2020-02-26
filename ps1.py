m=2000
n=3201
l=[]
for i in range(m,n):
  if i%5!=0 and i%7==0:
        l.append(str(i))
print(",".join(l))
