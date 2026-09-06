
'''
given an array arr of numbers, return the largest no in the array.
if the array is empty, return null 
'''

def largest(arr):
    if not arr:
        return "null"

    largest=None

    for num in arr:
        if largest is None or num > largest:
            largest=num

    return largest

print(largest([]))