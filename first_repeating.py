# First repeating element
def first_repeating(numbers):
    # Your code here
    seen=set()
    for i in numbers:
        if i in seen:
            return i
        seen.add(i)
print(first_repeating([4,5,6,4]))