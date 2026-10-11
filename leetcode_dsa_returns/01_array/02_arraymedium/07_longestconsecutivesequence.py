
'''
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

def longestconsecutive(nums):
    if not nums:
        return 0
    
    seen = set()
    length=1

    for num in nums:
        seen.add(num)

    for num in nums:
        if num-1 not in seen:
            isrunning=True
            count=1
            while isrunning:
                if num+1 in seen:
                    num=num+1
                    count+=1
                else:
                    isrunning=False

            length=max(length,count)

    return length

'''
not done yet 
dsa king prathamesh dalvi
'''


