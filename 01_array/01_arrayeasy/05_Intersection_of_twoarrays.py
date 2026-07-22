
'''
Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result must be unique, and you may return the result in any order.
'''

def intersection(arr1,arr2):
    inter=set()
    seen = set()

    for num in arr1:
            seen.add(num)

    for num in arr2:
        if num in seen:
            inter.add(num)

    return list(inter)

print(intersection([-1,-2,-3,4],[-3,4,1,2]))

'''
time complexity: O(n+m)
space complexity: O(n+m)
'''