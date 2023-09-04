def towSums(arr , target):
    prev = {}
    
    for  i , val in enumerate(arr):
        diff = target - val
        
        if diff in prev : 
            return [prev[diff] , i]
        
        prev[val] = i


print(towSums([2,7,11,15], 9))        