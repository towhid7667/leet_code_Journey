#didn't accept all the test
def threeSum(s):
    h = list(s)
    l = set()
    for i in range(len(h)):
        for j in range(i + 1, len(h)):
            if h[i] == h[j]:
                l.add(h[i])
                l.add(h[j])
    return len(l)          
                
        
print(threeSum("abcabcbb"))  
def longest_substring(s):
    s_set = set()
    l = 0
    k = 0
    for r in range(len(s)):
        while s[r] in s_set:
            s_set.remove(s[l])
            l += 1
        s_set.add(s[r])
        k = max(k, r-l + 1)        
    return k            
        
print(longest_substring("abcabcbb"))  
