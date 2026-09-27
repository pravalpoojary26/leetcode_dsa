
'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''

def sortedsquares(nums):
    left=0
    right=len(nums)-1
    pos=len(nums)-1

    sorted_nums=[1]*len(nums)

    while left<=right:
        if abs(nums[left])>abs(nums[right]):
            sorted_nums[pos]=nums[left]**2
            left+=1
        else:
            sorted_nums[pos]=nums[right]**2
            right-=1

        pos-=1

    return sorted_nums


print(sortedsquares([-5,-3,-2,-1]))