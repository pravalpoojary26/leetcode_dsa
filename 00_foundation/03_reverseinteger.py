
'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

def reverse(x):
    if x<0:
        x_copy=abs(x)
        x=int(str(x_copy)[::-1])
        x*=-1
    else:
        x=int(str(x)[::-1])

    if x< pow(-2,31) or x> pow(2,31) -1:
        return 0

    return x

print(reverse(1534236469))