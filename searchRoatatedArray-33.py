
#not all test case passed
def searchByRoatating(nums, target):
    n = (len(nums) // 2)
    print("sdsdsdsd", n)
    new_nums1 = nums[:n]
    new_nums2 = nums[n:]
    newArr = new_nums2 + new_nums1
    print(newArr)
    for i, value in enumerate(newArr):
        if value == target:
            return i 
    
    return -1
print(searchByRoatating([4, 5, 6, 7, 0, 1, 2], 0))


#not all test case passed
def searchByRoatating(nums, target):
     for i, value in enumerate(nums):
            if value == target:
                return i 
        
     return -1
print(searchByRoatating([4, 5, 6, 7, 0, 1, 2], 0))

