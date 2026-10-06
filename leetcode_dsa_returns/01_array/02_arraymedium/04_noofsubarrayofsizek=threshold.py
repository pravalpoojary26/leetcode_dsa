
'''
Given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.
'''

def numofsubarrays(arr,k,threshold):
    left=0
    right=k-1
    count=0
    array_sum=0

    for i in range(right+1):
        array_sum+=arr[i]

    if(array_sum/k)>=threshold:
        count+=1

    while right<len(arr)-1:
        right+=1
        array_sum+=arr[right]
        array_sum-=arr[left]
        left+=1

        if(array_sum/k)>=threshold:
            count+=1

    return count

print(numofsubarrays([11,13,17,23,29,31,7,5,2,3],3,5))


