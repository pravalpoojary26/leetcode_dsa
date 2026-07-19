
'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

def majority(arr):
    n = len(arr)

    count={}

    for num in arr:
        if num in count:
            count[num]+=1

        else:
            count[num]=1

        if (count[num])>((n//2)):
            return num
        
print(majority([2,3,1,2,1,2,2]))