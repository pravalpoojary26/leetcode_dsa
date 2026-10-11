
'''
Given a 0-indexed integer array nums, find the leftmost middleIndex 
(i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.
'''

def findmiddleindex(nums):
    left=0
    right=0
    total_sum=0
    for num in nums:
        total_sum+=num

    for i in range(len(nums)):
        right=total_sum-left-nums[i]

        if left==right:
            return i 

        left+=nums[i]

        return -1

print(findmiddleindex([2,5]))