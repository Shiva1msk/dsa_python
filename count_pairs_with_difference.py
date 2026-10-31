def count_pairs_with_difference(numbers, target):
    seen = set()
    count = 0
    for i in numbers:
        
        if i-target in seen: 
            count+=1
        if i+target in seen:
            count+=1
        seen.add(i)
    return count

print(count_pairs_with_difference([1, 5, 3, 4, 2],2))   