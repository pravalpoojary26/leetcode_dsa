
'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that
cover all the intervals in the input

do it aagain later 
'''

def merge_intervals(nums):
    nums.sort()
    result=[nums[0]]

    for i in range(1,len(nums)):
        current = result[-1]
        next = nums[i]

        if next[0]<=current[1]:
            current[1]=max(current[1],next[1])
        else:
            result.append(next)

    return result

print(merge_intervals([[1,4],[2,5],[3,7],[6,8]]))
        