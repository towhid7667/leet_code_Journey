# didn't pass all the test
def longest_consecutive(nums):
        k = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[j] - nums[i]) == 1:
                    k.add(nums[i])
                    k.add(nums[j])
        print(k)
        return len(k) 
print(longest_consecutive([100,4,200,1,3,2]))  

  
def longest_consecutive(nums):
    num_set = set(nums)
    longest_c = 0
    for i in nums:
        if (i - 1) not in num_set:
            length = 0
            while (i + length) in num_set:
                length += 1
            longest_c = max(length, longest_c)            
    return longest_c
print(longest_consecutive([100,4,200,1,3,2]))    