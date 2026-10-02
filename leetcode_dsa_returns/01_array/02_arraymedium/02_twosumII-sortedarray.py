
'''
You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.

Find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] 
of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.
'''

def twosum(nums,target):
    index1=0
    index2=len(nums)-1

    while index1<index2:
        if nums[index1]+nums[index2]==target:
            return [index1+1,index2+1]
        elif nums[index1]+nums[index2]>target:
            index2-=1
        else:
            index1+=1

print(twosum([-1,0],-1))
