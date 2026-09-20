
'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) 
and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
def mostwater(height):
    left=0
    right=len(height)-1
    container=0

    while left<right:
        width=right-left
        area = width*(min(height[left],height[right]))

        if area>container:
            container=area

        if height[left]>height[right]:
                right-=1
        else:
                left+=1

    return container

print(mostwater([5,5,5,5,5]))


        
