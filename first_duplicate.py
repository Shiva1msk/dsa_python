def find_first_duplicate(numbers):
    seen = set()

    for i in numbers:
        if i in seen:       # Blank 1: Check if i is already in seen
            return i  # Blank 2: Return the duplicate
        seen.add(i)            # Blank 3: Add i to seen

    return None