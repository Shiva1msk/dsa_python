n = int(input())
total=0
while n>0:
    digit=n%10
    n=n//10
    total+=digit
print(total)

