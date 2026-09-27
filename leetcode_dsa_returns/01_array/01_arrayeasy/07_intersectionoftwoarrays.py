
'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order
'''

def intersection(nums1,nums2):
    intersection=set()
    seen=set()

    for num in nums1:
        seen.add(num)

    for num in nums2:
        if num in seen:
            intersection.add(num)

    return list(intersection)

print(intersection([1,2,2,1],[2,2]))