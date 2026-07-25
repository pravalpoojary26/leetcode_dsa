
'''
Find All Numbers Disappeared in an Array
'''

def disappeared(arr):
    present = set(arr)
    missing =[]

    for i in range(1,len(arr)+1):
        if i not in present:
            missing.append(i)

    return missing

print(disappeared([2,3,2,1,5]))

    