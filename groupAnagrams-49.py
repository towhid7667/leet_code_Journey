from collections import defaultdict
def groupAnagrams(strs):
        m = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord("a")] += 1
            m[tuple(count)].append(i)    
            
        return list(m.values())
    
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))      




def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    mp ={}
    for s in strs:
        f = str(sorted(s))
        if f not in mp:
            mp[f] = []
        mp[f].append(s)
    return list(mp.values())  