
'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and 
right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''

def sumquery(nums,left,right):
    current_sum=0
    while left<=right:
        current_sum+=nums[left]
        left+=1

    return current_sum

print(sumquery([-2, 0, 3, -5, 2, -1],0,5))

-2 , -2 , 1 , -4 ,-2 ,-3    