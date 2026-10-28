def gcd(a,b):
    n=min(a,b)
    while n>0:
        if a%n==0 and b%n==0:
            return n
        n-=1

def lcm(a,b):
    lcm=(a*b)//gcd(a,b)
    print(lcm)

lcm(4,6)