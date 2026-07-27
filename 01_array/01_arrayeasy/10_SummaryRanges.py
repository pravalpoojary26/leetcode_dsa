
'''
'''

def summaryrange(arr):
    if not arr:
        return []
    
    start = arr[0]

    ans=[]

    for i in range(len(arr)-1):
        if arr[i]+1 != arr[i+1]:

            if start == arr[i]:
                ans.append(str(start))

            else:
                ans.append(f'{start}->{arr[i]}')

            start=arr[i+1]

    if start==arr[-1]:
        ans.append(str(start))

    else:
        ans.append(f'{start}->{arr[-1]}')

    return ans 

print(summaryrange([0,1,2,4,5,7]))
