
'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
'''

def topfrequent(nums,k):
    count={}

    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1

    count= dict(sorted(count.items(),key=lambda x : x[1],reverse=True))

    return list(count.keys())[:k]

print(topfrequent([4,4,4,6,6,2,2,2,2],3))

