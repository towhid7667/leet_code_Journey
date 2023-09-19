import math
def ProductsCount(nums):
    b = []
    for i in nums:
        nums.remove(i)
        b.append(math.prod(nums))
        nums.insert(0, i)
    return b 



# [2,3,4,5]
# [1,2,6,24] pre
# [60,20,5,1]post
# [60,40,30,24]
def ProductsCount(nums):
    l = len(nums)
    p = [1] * l
    
    for i in range(1, l):
        p[i] = p[i-1] * nums[i - 1]
    r = nums[-1]
    for i in range(l - 2, -1 , -1):
        p[i] *= r
        r *= nums[i]
        
    return p    

print(ProductsCount([2,3,4,5]))


def ProductsCount(nums):
        l = len(nums)
        k = [1] * l

        pre = 1
        for i in range(l):
            k[i] = pre
            pre *= nums[i]
        post = 1

        for i in range(l -1, -1 ,-1):
            k[i] *= post
            post *= nums[i]
        return k 

print(ProductsCount([2,3,4,5]))
            
        
    