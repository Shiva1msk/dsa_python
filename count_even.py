def count_even(numbers):
    even_count=0
    for i in numbers:
        if i%2==0:
            even_count+=1
    return even_count