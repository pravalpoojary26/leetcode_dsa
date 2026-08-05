
'''
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

def threesum(nums):
    triplets=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]==nums[j]==nums[k]:
                    continue
                elif (nums[i]+nums[j]+nums[k]==0):
                    triplets.append([nums[i],nums[j],nums[k]])

    return triplets

print(threesum([-1,0,1,2,-1,-4]))
