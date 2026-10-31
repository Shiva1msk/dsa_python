def numcon(numbers,k):
    l2=[]
    for number in numbers:
        text=str(number)
        l1=list(text)
        l1.sort(reverse=True)
        new=int(''.join(l1))
        l2.append(new-number)
    l2.sort(reverse=True)

    return sum(numbers)+sum(l2[:k])
print(numcon([102, 90, 14],2))
