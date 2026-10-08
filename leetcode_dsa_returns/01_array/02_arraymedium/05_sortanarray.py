
'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and 
with the smallest space complexity possible.
'''

def sortarray(nums):
    temp = [1] * len(nums)

    def mergesort(left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        mergesort(left, mid)
        mergesort(mid + 1, right)

        i = left
        j = mid + 1
        k = 0

        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1

        for x in range(k):
            nums[left + x] = temp[x]

    mergesort(0, len(nums) - 1)
    return nums

print(sortarray([5,2,3,1]))

'''
solve by other sorting algorithms also 
'''
        




    



