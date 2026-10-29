def first_non_repeating(numbers):
    freq = {}

    # Count each number here
    for i in numbers:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in numbers:
        if freq[i]==1:
            return i
print(first_non_repeating([4,5,6,4,5,7]))