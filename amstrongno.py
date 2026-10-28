n = int(input())
temp=n
temp1=n
total=0
count=0
while n>0:
    digit=n%10
    n=n//10
    count+=1

while temp>0:
    digit=temp%10
    temp=temp//10
    total=total+digit**count

if temp1==total:
    print("amstrong")
else:
    print("not amstrong")

