
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

def longestcommonprefix(arr):
    prefix = arr[0]

    for i in range(1,len(arr)):
        while arr[i].startswith(prefix)==False:
            prefix=prefix[:-1]

    return prefix

print(longestcommonprefix(["dog","racecar","car"]))