
'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and
return this value. Any answer with a calculation error less than 10-5 will be accepted.
'''

def findmaxavg(nums,k):
    left=0
    right=k-1
    window_sum=0
    max_avg=-2**31
    for i in range(right+1):
        window_sum+=nums[i]

    max_avg=window_sum/k

    while right<len(nums)-1:
        right+=1
        window_sum+=nums[right]
        window_sum-=nums[left]
        left+=1

        max_avg=max(max_avg,window_sum/k)

    return max_avg

print(findmaxavg([7,4,5,8,8,3,9,8,7,6],7))

