
'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''
#BRUTE FORCE APPROACH
def rotate(nums,k):
    k=k%len(nums)
    temp=nums[-k:]

    for i in range(len(nums)-1,k-1,-1):
        nums[i]=nums[i-k]

    for i in range(k):
        nums[i]=temp[i]

    return nums

print(rotate([-1,-100,3,99],2))

'''
TIME COMPLEXITY : O(N)
SPACE COMPLEXITY : O(N)
'''
    