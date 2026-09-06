
'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
and with the smallest space complexity possible.
'''

def mergesort(nums):
    if len(nums)>1:
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]

        mergesort(left)
        mergesort(right)

        i = 0
        j =0
        k =0

        while i<len(left) and j <len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1

    return nums

print(mergesort([20,26,25,9,11,1]))
 