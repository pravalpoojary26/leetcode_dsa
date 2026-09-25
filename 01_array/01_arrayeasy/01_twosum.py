
'''
You are given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
'''

def twosum(nums,target):
    #we will store nos here with thier indexes
    count={}

    for i in range(len(nums)):
        #it will calculte the number it needs 
        number=target-nums[i]
        #and will check here if its present or not 
        if number in count:
            return count[number],i
        else:
            count[nums[i]]=i

print(twosum([0,4,3,0],0))

'''
Time complexity : O(n)
Space complexity : O(n)

Test cases :

[2, 7, 11, 15] , 9
[3, 3] , 6
[3, 2, 4] , 6
[-3, 4, 3, 90] , 0 
[0, 4, 3, 0] , 0
'''