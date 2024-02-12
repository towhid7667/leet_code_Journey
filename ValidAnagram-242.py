# didn't pass all the test case
def valid_anagram(s, t):
    k = []
    for i in t:
        if i in s:
            k.append(i)
    print(k)        
    if len(k) == len(s) and t == ''.join(k):
        return True
    return False

print(valid_anagram("aacc", "ccac"))

def valid_anagram(s, t):
    k = []
    l = []
    for i in t:
       a = s.count(i)
       b = t.count(i)
       k.append(a)
       l.append(b)
    print("sd", k)   
    print("sd", l)   
    if k == l and len(s) == len(t):
        return True
    return False
print(valid_anagram("ab", "a"))



def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
