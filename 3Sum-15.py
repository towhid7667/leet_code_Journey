# time limit exceeded

def threeSum(nums):
    g = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1 , n):
                l = nums[i] + nums[j] + nums[k]
                if l == 0:
                    o = sorted([nums[i], nums[j] , nums[k]])
                    g.add(tuple(o))

    if len(g) == 0:
        return [] 
    else: 
        return g          
print(threeSum([-1,0,1,2,-1,-4]))        