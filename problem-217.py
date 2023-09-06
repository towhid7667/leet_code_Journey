
#runtime
def containsDuplicate(nums):
    b = []
    print("====", len(nums))
    for i in nums:
        print(i)
        nums.remove(i)
        # print(nums)
        print(len(nums))
        
        if i in nums:
            b.append(i)
            b.append(i)
            
            
    print(b)                
    if len(b) > 1:
        return True
    else:
        return False
    
 #runtime   
def containsDuplicate(nums):
    b  = []
    for i in nums:
        if i in b:
            return True
        else:
            b.append(i)
    return False 


 #runtime   
def containsDuplicate(nums):
    b  = []
    for num in nums:
        if nums.count(num) > 1:
            b.append(num)
    if len(b) > 0:
        return True
    else:
        return False
 #Accepted           
def containsDuplicate(nums):
    b  = set()
    for i in nums:
        if i in b:
            return True
        else:
            b.add(i)
    return False 
            
    
