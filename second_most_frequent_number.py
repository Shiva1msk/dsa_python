def second_most_frequent_number(numbers):
    freq={}
    for i in numbers:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    frequencies=sorted(set(freq.values()),reverse=True)
    if len(frequencies)<2:
        return None
    second_freq=frequencies[1]
    for num,count in freq.items():
        if count==second_freq:
            return num
    

print(second_most_frequent_number([5, 5, 5, 2, 2, 8, 8, 8]))