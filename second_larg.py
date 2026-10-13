
def find_second_largest(numbers):
    if not numbers:
        return "Empty list"

    maxele = numbers[0]
    second_max = -float("inf")

    for i in numbers:
        if i > maxele:
            second_max = maxele
            maxele = i
        elif i != maxele and i > second_max:
            second_max = i

    if second_max == -float("inf"):
        return "No second largest number"

    return second_max


print(find_second_largest([4, 7, 2, 9, 7, 3]))
print(find_second_largest([9, 9, 9]))
print(find_second_largest([]))
