
def find_smallest(numbers):
    min_element = numbers[0]

    for i in numbers:
        if i < min_element:
            min_element = i

    return min_element


numbers = [8, 3, 12, 1, 6]
print(find_smallest(numbers))
