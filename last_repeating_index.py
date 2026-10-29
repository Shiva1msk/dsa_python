def last_repeating_index(numbers):
    seen=set()
    index=None

    for i,v in enumerate(numbers):
        if v in seen:
            index=i
        seen.add(v)
    return index
print(last_repeating_index([2,3,4,4,5]))
print(last_repeating_index([2, 3, 4, 5]))
print(last_repeating_index([1, 2, 1, 3, 2]))



