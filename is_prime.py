def is_prime(a):
    if a<=1:
        return False

    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

n=is_prime(21)
print(n)