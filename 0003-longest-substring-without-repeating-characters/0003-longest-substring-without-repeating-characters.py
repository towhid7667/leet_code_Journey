class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        converted_set = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in converted_set:
                converted_set.remove(s[left])
                left += 1
            converted_set.add(s[right])
            result = max(result , right - left + 1)
        return result        

        