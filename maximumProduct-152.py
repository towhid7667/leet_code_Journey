
# memroy limit crossed, thats it -
def maxProductSubArray(nums):
    n = len(nums)
    combinations = []
    for i in range(n + 1):
        for j in range(i):
            combination = nums[j:i]
            combinations.append(combination)       
    OOP = []
    for i in combinations:
        sum = 1
        for j in i:
            sum *= j
        OOP.append(sum)
    print(OOP)    
    return max(OOP)  

print(maxProductSubArray([-3,-1,-1]))    

#  didn't pass all the test case 
def maxProductSubArray(nums):
    maxProduct = nums[0]
    currentProduct = 1
    print(maxProduct)
    for i in nums:
        if currentProduct == 0:
            currentProduct = 1  
        currentProduct *= i     
        maxProduct = max(maxProduct, currentProduct)    
    return maxProduct

print(maxProductSubArray([-1,4,-4,5,-2,-1,-1,-2,-3]))    

#  Accepted
def maxProductSubArray(nums):
    maxProduct = nums[0]
    current_max, current_min = 1 , 1 
    for i in nums:
        t =  i * current_max    
        current_max = max(i * current_max, i * current_min, i)        
        current_min = min(t , i * current_min, i)        
        maxProduct = max(maxProduct, current_max)
    return maxProduct

print(maxProductSubArray([-1,4,-4,5,-2,-1,-1,-2,-3]))     