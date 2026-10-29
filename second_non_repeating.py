def second_non_repeating(numbers):
    freq = {}
    count=0

    # Count each number's frequency
    for i in numbers:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    for i in numbers:
        if freq[i]==1:
            count+=1
        if count==2:
            return i
print(second_non_repeating([3,4,3,4,5,7,8]))