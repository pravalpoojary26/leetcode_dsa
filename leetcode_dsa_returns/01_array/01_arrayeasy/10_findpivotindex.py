
'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is 
equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''

def pivotindex(nums):
    total_sum = sum(nums)
    left=0
    right=0

    for i in range(len(nums)):
        right=total_sum-left-nums[i]

        if left==right:
            return i

        left+=nums[i]

    return -1

print(pivotindex([1,7,3,6,5,6]))

'''
total_sum =28
left =0, right=27
left=1, right=20
left=8,right=17
left=11,right=11
'''