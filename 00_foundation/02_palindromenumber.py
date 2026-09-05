
'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

def palindrome(x):
    if x<0:
        return False

    x_copy = int(str(x)[::-1])

    if x == x_copy:
        return True

    return False

print(palindrome(1221))