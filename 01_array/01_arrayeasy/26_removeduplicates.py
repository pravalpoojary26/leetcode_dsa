
'''
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. 
After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. 
The remaining elements beyond index k - 1 can be ignored.
'''

def removeduplicates(nums):
    #Assigning two pointer 
    left=0
    right=0

    while right<len(nums):
        #IF values are not equal then first will increment left and then assign it 
        if nums[left]!=nums[right]:
            left+=1
            nums[left]=nums[right]
        #Otherwise will just increment right to check other elements 
        else:
            right+=1

    #Unique elemennts 
    return left+1

print(removeduplicates([-3,-3,-2,-1,-1,0,0,0,2]))   

'''
Time Complexity is O(n)
Space Complexity is O(1)

Test Cases
[1,1,2]
[0,0,1,1,1,2,2,3,3,4]
[1,2,3,4,5]
[1,1,1,1,1]
[-3,-3,-2,-1,-1,0,0,0,2]
'''


