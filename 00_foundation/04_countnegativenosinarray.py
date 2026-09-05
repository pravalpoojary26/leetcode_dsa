
'''
given an array arr of numbers,return the count of elements less than 0
'''

def negative(arr):
    count=0
    for num in arr:
        if num<0:
            count+=1

    return count

print(negative([]))
