def count_pairs(numbers, target):
    seen={}
    count=0
    for i in numbers:
        expeced=target-i
        if expeced in seen:
            count+=seen[expeced]
        seen[i]=seen.get(i,0)+1
    return count

result=count_pairs([3, 3, 3, 3], 6)
print(result)