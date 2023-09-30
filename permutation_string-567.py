# Output Limit Exceeded
from itertools import permutations
def checkInclusion(s1,  s2):
        permutations_list1 = list(permutations(s1))


        print("1111", permutations_list1)
      

        # Print the permutations
        for k in permutations_list1:
            l = ''.join(k)
            if l in s2:
                return True
        return False
print(checkInclusion("ab", "eidbaooo"))  
        
# Output Limit Exceeded
 
def checkInclusion(s1,  s2):
    unique_permutations = set()

    def generate_permutations(prefix, remaining_str):
        if not remaining_str:
            unique_permutations.add(prefix)
        for i in range(len(remaining_str)):
            generate_permutations(prefix + remaining_str[i], remaining_str[:i] + remaining_str[i+1:])

    generate_permutations('', s1)

    
    print(unique_permutations)
    for i in unique_permutations:
        if i in s2:
            return True
    return False 


     
print(checkInclusion("ab", "eidbaooo"))


def checkInclusion(s1,  s2):
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord("a")
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord("a")
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26
    


     
print(checkInclusion("ab", "eidbaooo"))

