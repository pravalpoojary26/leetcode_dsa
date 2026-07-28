
'''
Given an integer numRows, return the first numRows of Pascal's Triangle.

In Pascal's Triangle:

The first and last element of every row is 1.
Every other element is the sum of the two elements directly above it.
'''

def pascal(n):
    triangle=[]

    for i in range(n):
        row = [1]*(i+1)

        for j in range(1,i):
            row[j]=triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle

print(pascal(5))

