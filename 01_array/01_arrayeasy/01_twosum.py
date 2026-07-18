
'''
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
'''

def twosum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j])==target:
                return (i,j)
            
print(twosum([1,4,7,3,9],10))

'''
Time Complexity : O(n^2)
Space Complexity: O(1)
'''
