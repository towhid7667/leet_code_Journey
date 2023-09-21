# # time limit exceeded

def threeSum(nums):
    g = set()
    n = len(nums)
    for i in range(n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1 , n):
                l = nums[i] + nums[j] + nums[k]
                if l == 0:
                    o = sorted([nums[i], nums[j] , nums[k]])
                    g.add(tuple(o))

    if len(g) == 0:
        return [] 
    else: 
        return list(g)          
print(threeSum([-1,0,1,2,-1,-4]))        

def threeSum(nums):
     k = []
     nums.sort()
     for i , value in enumerate(nums):
         if i > 0 and value == nums[i - 1]:
             continue
         l , r = i + 1 , len(nums) - 1
         while l < r:
             sums = value + nums[l] + nums[r]
            #  the number are sorted so we need to decrease or increase
             if sums < 0:
                 l += 1
             elif sums > 0:
                 r -= 1
             else:
                 k.append([value , nums[l] , nums[r]])
                 l += 1
                 while nums[l] == nums[l - 1] and l < r:
                     l += 1   
     return k                      
                 
              
print(threeSum([-1,0,1,2,-1,-4]))        