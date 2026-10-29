def second_most_frequent(text):
    freq={}
    for i in text:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    frequencies = sorted(set(freq.values()), reverse=True)
    if len(frequencies)<2:
        return None
    second_most_frequent=frequencies[1]
    for char, count in freq.items():
        if count== second_most_frequent:
            return char
        

print(second_most_frequent("aaaabccc"))