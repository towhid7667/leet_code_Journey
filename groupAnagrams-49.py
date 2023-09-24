def groupAnagrams(strs):
        m = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord("a")] += 1
            m[tuple(count)].append(i)    
            
        return m.values()  
    
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))      