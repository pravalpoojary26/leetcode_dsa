
'''
given an array arr of numbers, return the smallest number in the array.
if the array is empty return null
'''

def smallest(arr):
    if not arr:
        return "null"

    smallest=None

    for num in arr:
        if smallest is None or num < smallest:
            smallest=num

    return smallest

print(smallest([]))