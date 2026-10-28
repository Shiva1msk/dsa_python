num=[0,1,0,2,0,3]
num1=[]
count=0
for i in num:
    if i!=0:
        num1.append(i)
    else:
        count+=1

for i in range(count):
    num1.append(0)

print(num1)
