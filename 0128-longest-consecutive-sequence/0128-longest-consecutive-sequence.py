class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        longest = 0
        for i in nums:
            length = 0
            if (i - 1) not in new_set:
                while (i + length) in new_set:
                    length += 1
                longest = max(longest , length)    
        return longest        
