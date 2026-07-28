
'''
Given an integer array nums, find the pivot index.

A pivot index is an index where:

Sum of all elements to the left = Sum of all elements to the right

If there are multiple pivot indexes, return the leftmost one.

If none exists, return -1.
'''

def pivot(arr):
    total_sum=sum(arr)
    left=0
    right=0

    for i in range(len(arr)):
        right=total_sum-left-arr[i]

        if left==right:
            return i

        left+=arr[i]

    return -1

print(pivot([-1,-1,-1,0,1,1]))

