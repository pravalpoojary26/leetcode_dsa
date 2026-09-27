
'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

def maximumsubarray(nums):
    current_sum=0
    max_sum=-2**31

    for num in nums:
        current_sum+=num
        max_sum=max(max_sum,current_sum)
        if current_sum<0:
            current_sum=0

    return max_sum

print(maximumsubarray([5,4,-1,7,8]))