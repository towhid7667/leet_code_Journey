def findMinByRoatating(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                
    return nums[0]     
print(findMinByRoatating([5,4,-1,7,8]))   