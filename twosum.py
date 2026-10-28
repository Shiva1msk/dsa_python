def two_sum(numbers, target):
    seen={}
    for i,v in enumerate(numbers):
        excepted=target-v
        if excepted in seen:
            return seen[excepted],i
        seen[v]=i

result=two_sum([2,7,8,9],9)
print(result)