# initially accepted
# def containerWater(height):
#     unique_list = list(set(height))
#     l = max(unique_list)
#     if len(unique_list) == 1:
#         return l * l
#     unique_list.remove(l)
#     j = max(unique_list)
    
#     return j * j

# print(containerWater([1,1]))     

# l = max(height)
#         height.remove(l)
#         j = max(height)
        
#         return j * j

# time limt exceed

def containerWater(height):
    res = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area  = (j - i) * min(height[j] , height[i])
            res = max(res, area)
    return res

print(containerWater([4,3,2,1])) 


# if height[-1] == h or height[-1] > h or height[-1] < h: 
#             return height[-1] * height[-1]
def containerWater(height):
        res = 0
        l , r = 0 , len(height) - 1
        while l < r:
            area  = (r - l) * min(height[l] , height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] < height[r]:
                r -= 1
            else:
                r -= 1
        return res  

print(containerWater([4,3,2,1])) 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l , r = 0 , len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res             
