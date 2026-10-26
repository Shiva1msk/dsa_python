def count_odd(numbers):
    odd_count=0
    for i in numbers:
        if i%2!=0:
            odd_count+=1
    return odd_count