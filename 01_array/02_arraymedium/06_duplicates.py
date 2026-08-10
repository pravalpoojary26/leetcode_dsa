
'''
287 -> find the dupliactes 
do it aggain without looking and try all the test cases 
'''

def duplicates(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow =nums[0]
    while True:
        slow = nums[slow]
        fast = nums[fast]

        if slow== fast:
            return nums[slow]


