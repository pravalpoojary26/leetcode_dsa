
num = [1,2,3,4,5]

#MAximum subarray brute force approach
max_sum=0
for i in range(len(num)):
    current_sum=0
    for j in range(i,len(num)):
        current_sum+=num[j]
        max_sum=max(current_sum,max_sum)

print(max_sum)