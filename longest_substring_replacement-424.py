# length - maxFreq <= k
def longest_substring_replacement(s, k):
    count = {}
    result = 0
    
    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        result = max(result, r - l + 1)    
    
    return result     
        
print(longest_substring_replacement("abcabcbb", 2))  
def longest_substring_replacement(s, k):
    count = {}
    result = 0
    
    l = 0
    max_freq = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_freq = max(max_freq, count[s[r]])
        while (r - l + 1) - max_freq > k:
            count[s[l]] -= 1
            l += 1
        result = max(result, r - l + 1)    
    
    return result     
        
print(longest_substring_replacement("abcabcbb", 2))  