def second_most_frequent(text):
    freq={}
    for i in text:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    high_feq=0
    second_most_frequent=None
    for i in freq.values():
        if i>high_feq:
            second_most_frequent=high_feq
            high_feq=i
        elif i!=high_feq and i>second_most_frequent:
            second_most_frequent=i
        
    

    
    

    return second_most_frequent

print(second_most_frequent("aaaabccc"))