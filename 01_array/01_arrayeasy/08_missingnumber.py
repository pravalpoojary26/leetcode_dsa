
'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
'''

def missingnumber(nums):
    n = len(nums)
    expected_sum=0
    actual_sum=0

    #Sum of every nos from range 0 to n
    for i in range(n+1):
        expected_sum+=i

    #Sum of given array 
    for i in range(len(nums)):
        actual_sum+=nums[i]

    #Fidning missing number
    missingnumber = expected_sum - actual_sum
    
    return missingnumber


print(missingnumber([9,6,4,2,3,5,7,0,1]))