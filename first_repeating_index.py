def first_repeating_index(numbers):
    seen = set()

    for index, num in enumerate(numbers):
        # What condition checks whether num appeared before?
        # If it did, return index.
        if num in seen:
            return index
        seen.add(num)

        # Otherwise, add num to seen.
print(first_repeating_index([4,5,4,4,5,6]))