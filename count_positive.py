def count_positive(numbers):
    positive_count=0
    for i in numbers:
        if i>0:
            positive_count+=1
    return positive_count