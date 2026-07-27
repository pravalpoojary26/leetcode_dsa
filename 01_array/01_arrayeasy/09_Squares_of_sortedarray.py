
'''
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order
'''

def squares(arr):
    left = 0
    right = len(arr)-1

    ans = [0]*len(arr)
    position= len(arr)-1

    while left<=right:
        if arr[left]**2 > arr[right]**2:
            ans[position]= arr[left]**2
            left+=1
        else:
            ans[position]= arr[right]**2
            right-=1

        position-=1

    return ans

print(squares([-2,-1,0,1,2]))

'''
Time Complexity : O(n)
Space Complexity : O(n)
'''