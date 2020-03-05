#accessing the elements in tuple

t1=(1,2,3,4,5)
t2=(5,6,7,8,9)
print(t1[0])
print(t2[0])


#updating the elements in tuple

t1=(1,2,3,4,5)
t2=(6,7,8,9)
t3=t1+t2
print(t3)

#deleting the elements of the tuple
#pass the elements in tuple
t2=(5,6,7,8,9)
l=[]
for i in t2:
    l.append(i)
l.remove(l[2])
t=tuple(l)
print(t)

#built in function in tuples

t1=(5,6,7,8,9)
t2=(1,2,3,4,0)
print(min(t1))

#set operation on tuples like union,intersection,difference

#union of two tuples
t1=(1,2,3,4,5)
t2=(6,7,8,9,0)
for i in t2:
    if i not in t1:
        t1=t1+t2
print(t1)

#intersection of two tuples

t1=(1,2,3,4,5)
t2=(6,7,5,8,3)
l=[]
for i in t1:
    if i in t2:
       l.append(i)
       t=tuple(l)
print(t)

       



