

# O(n)

def towSums(arr , target):
    prev = {}
    
    for  i , val in enumerate(arr):
        diff = target - val
        
        if diff in prev : 
            return [prev[diff] , i]
        
        prev[val] = i


print(towSums([2,7,11,15], 9))        


# O(n2)
def towSums(arr , target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1 , n):
            if arr[i] + arr[j] == target:
                return [i , j]
print(towSums([2,7,11,15], 9)) 


