
'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

def runningsum(nums):
    current_sum=0
    for i in range(len(nums)):
        current_sum+=nums[i]
        nums[i]=current_sum

    return nums

print(runningsum([3,1,2,10,1]))