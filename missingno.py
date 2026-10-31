def find_missing(num):
    n=len(num)+1
    actual=n*(n+1)//2
    total=0
    for i in num:
        total+=i
    print(actual-total)

find_missing([3,4,2,1,5,7])
