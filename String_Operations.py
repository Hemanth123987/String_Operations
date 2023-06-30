s=input().split()
print(len(s))
l=[]
for i in s:
    i=i.lower()
    l.append(i)
s1=set(l)
l1=[]
for i in s1:
    count=l.count(i)
    l2=[i,count]
    l1.append(l2)
l3=[]
for i in l1:
    l3.append(i[1])
m=max(l3)
for i in l1:
    if(i[1]==m):
        print(i[0])
l4=[]
for i in s:
    l4.append(len(i))
print(max(l4))