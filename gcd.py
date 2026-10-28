a = int(input())
b = int(input())

n=min(a,b)

while n>0:
    if a%n==0 and b%n==0:
        print("gcd:",n)
        break
    n-=1
    

