def towSums(arr , target):
    prev = {}
    new_numbers = sorted(arr)
    print(new_numbers)

    for i, val in enumerate(new_numbers):
        diff = target - val
        if diff in prev:
            return [prev[diff] + 1 , i + 1]
        prev[val] = i   


print(towSums([2,7,11,15], 9))  


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l + 1 , r + 1]        