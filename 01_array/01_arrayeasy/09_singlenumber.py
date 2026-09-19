
'''
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and
use only constant extra space.
'''

def singlenumber(nums):
    xor=0
    for i in nums:
        xor^=i

    return xor

print(singlenumber([4,4,2,6,6]))