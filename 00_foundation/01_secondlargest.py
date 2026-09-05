
'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s,
or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.
'''

def secondlargest(s):
    if s.isalpha():
        return -1

    largest=-1
    secondlargest=-1
    for ch in s:
        if ch.isdigit():
            if int(ch) > largest:
                secondlargest=largest
                largest=int(ch)
            elif int(ch)> secondlargest and largest!=int(ch):
                secondlargest=int(ch)

    return secondlargest

print(secondlargest("abcdef"))


