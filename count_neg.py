def count_negative(numbers):
    negative_count=0
    for i in numbers:
        if i<0:
            negative_count+=1
    return negative_count