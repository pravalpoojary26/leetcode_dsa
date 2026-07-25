
'''
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
'''

def thirdlargest(arr):
    first=second=third=None

    for num in arr:
        if num in (first,second,third):
            continue

        if first is None or (num>first):
            third=second
            second=first
            first=num

        elif second is None or (num>second):
            third=second
            second=num

        elif third is None or (num>third):
            third=num

    return third if third is not None else first

        
            