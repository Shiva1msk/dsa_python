def find_missing(num):
    n=len(num)
    actual=n*(n+1)//2
    total=0
    for i in num:
        total+=i
    print(actual-total)

find_missing([0,3,1])
