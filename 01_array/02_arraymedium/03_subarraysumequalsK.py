
'''
Given an array of integers nums and an integer k, return the total number of subarrays
whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''
def subarray(nums,k):
    arrays=[]

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==k:
                arrays.append(nums[i])

            if (nums[i]+nums[j])==k:
                arrays.append([nums[i],nums[j]])

    return arrays

print(subarray([1,1,1],2))
