class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in val:
                return [val[diff], i]
            val[v] = i
