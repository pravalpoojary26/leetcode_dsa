
'''
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates,
 return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. 
The remaining elements beyond index k - 1 can be ignored.
'''

def removedupliactes(nums):
    slow=0
    fast=1
    while fast<len(nums):
        if nums[slow]==nums[fast]:
            fast+=1
        else:
            slow+=1
            nums[slow]=nums[fast]

    k = slow+1

    return nums,k

print(removedupliactes([1,1]))

'''
Time Complexity  → O(n)
Space Complexity → O(1)
'''