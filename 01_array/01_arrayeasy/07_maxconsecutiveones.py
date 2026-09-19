
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

def maxones(nums):
    count=0
    maxcount=0

    for i in nums:
        if i==0:
            maxcount=max(maxcount,count)
            count=0

        else:
            count+=1

    maxcount=max(maxcount,count)

    return maxcount

print(maxones([0,1,1,1,0,1,1]))
