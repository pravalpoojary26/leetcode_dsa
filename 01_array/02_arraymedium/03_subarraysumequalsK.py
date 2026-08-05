
'''
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

def subarraysum(nums,k):
    hasmap={0:1}
    current_sum=0
    count=0

    for num in nums:
        current_sum+=num

        need = current_sum-k

        if need in hasmap:
            count+=hasmap[need]

        if current_sum in hasmap:
            hasmap[current_sum]+=1

        else:
            hasmap[current_sum]=1

    return count

print(subarraysum([0,0,0],0))
            
