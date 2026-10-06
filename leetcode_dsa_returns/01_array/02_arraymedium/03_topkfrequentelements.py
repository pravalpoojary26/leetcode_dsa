
'''
Given an integer array nums and an integer k,return the k most frequent elements. 
You may return the answer in any order.
'''

def topkfrequent(nums,k):
    count={}
    freq = [[] for i in range(len(nums)+1)]

    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1

    for num in count:
        frequency=count[num]
        freq[frequency].append(num)

'''
Not done yet.....
'''



