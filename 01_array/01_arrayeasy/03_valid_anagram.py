
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise
'''

def anagram(s,t):
    if len(s)!=len(t):
        return False
    
    count ={}

    for ch in s.lower():
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1

    for ch in t.lower():
        if ch not in count:
            return False
        
        count[ch]-=1

        if count[ch]<0:
            return False
        
    return True
        
print(anagram('Praval','aapvlr'))

'''
Time Complexity : O(n)
Space Complexityy : O(n)
'''