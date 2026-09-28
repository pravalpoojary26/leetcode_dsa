
'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
'''

'''
This is O(n) time complexity and O(n) space complexity 
Do this in O(1) space complexity once u learn mayer boorn algorithm voting 
'''
def majorityelement(nums):
    count={}

    for num in nums:
        if num in count:
            count[num]+=1

            if count[num]>(len(nums)/2):
                return num

        else:
            count[num]=1

print(majorityelement([2,2,1,1,1,2,2]))