
'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative
'''

def rotate(nums,k):
    if not nums:
        return

    k = k%len(nums)

    left=0
    right=len(nums)-1
    while left<right:
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        left+=1
        right-=1

    left=0
    right=k-1
    while left<right:
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        left+=1
        right-=1

    left=k
    right=len(nums)-1
    while left<right:
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        left+=1
        right-=1

    return nums

print(rotate([1],100))

