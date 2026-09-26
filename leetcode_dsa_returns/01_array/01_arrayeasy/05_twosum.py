
'''
You are given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
'''

def twosum(nums,target):
    seen={}

    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [seen[need],i]

        seen[nums[i]]=i

print(twosum([3,3],6))