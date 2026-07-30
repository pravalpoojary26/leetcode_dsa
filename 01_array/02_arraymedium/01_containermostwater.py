
'''
You are given an integer array height of length n.There are n vertical lines drawn such
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

def mostwater(arr):
    left=0              #Space Complexity->1
    right=len(arr)-1    #Space Complexity->1
    container=0         #Space Complexity->1

    while left!=right:  #Time Complexity->n
        width=right-left
        area =width*(min(arr[left],arr[right]))

        if area>container:
            container=area

        if arr[left]>arr[right]:
            right-=1
        else:
            left+=1

    return container

print(mostwater([2,3,10,5,7,8,9]))

'''
Time Complexity: O(n) because one pointer moves each iteration until the pointers meet.
Space Complexity: O(1) because only a constant number of extra variables are used
'''