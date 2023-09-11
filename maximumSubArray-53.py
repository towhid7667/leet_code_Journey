
#how to find subArray
def subArray(nums):
    n = len(nums)
    combinations = []
    for i in range(n + 1):
        for j in range(i):
            combination = nums[j:i]
            combinations.append(combination) 
    return combinations



print(subArray([5,4,-1,7,8]))       


# memory limit crossed
def maxSubArray(nums):
    n = len(nums)
    combinations = []
    for i in range(n + 1):
        for j in range(i):
            combination = nums[j:i]
            combinations.append(combination)       
    OOP = []
    for i in combinations:
        sum = 0
        for j in i:
            sum += j
        OOP.append(sum)
    print(OOP)    
    return max(OOP)    
                
                
print(maxSubArray([5,4,-1,7,8]))             

#Accepted o(n)
def maxSubArray(nums):
    maxSub = nums[0]
    currentSum = 0
    for i in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += i
        maxSub = max(maxSub , currentSum)  
        
    return maxSub          
print(maxSubArray([5,4,-1,7,8]))                     