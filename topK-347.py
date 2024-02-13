# didn't pass all the test case
def topKList(nums, k):
    l = []
    for i in range(len(nums)):
        for j in range (i + 1, len(nums)):
            if nums[j] - nums[1] == 1:
                l.append(nums[i])
                l.append(nums[j])   
            
    if len(nums) <= 1:
        return nums
    return l[:k]

print(topKList([1,1,1,2,2,3], 2))

# didn't pass all the test case

def topKList(nums, k):
    b ={}
    for i , value in enumerate(nums):
        p = nums.count(value)
        b[p] = value
    print(b)
    selected_values = []

    for key, value in b.items():
        if key >= k:
            selected_values.append(value)
    return selected_values

print(topKList([1,1,1,2,2,3], 2))



# didn't pass time limit test case

def topKList(nums, k):
    f = {}
    for i in nums:
        a = nums.count(i)
        f[i] = a
    sorted_dict = dict(sorted(f.items(), key=operator.itemgetter(1), reverse=True))
    j = list(sorted_dict.keys())  
    return j[:k]

print(topKList([1,1,1,2,2,3], 2))



# Accepted

def topKList(nums, k):
    f = {}
    for i in nums:
        if i in f:
            f[i] += 1
        else: f[i] = 1
    
    j = sorted(f, key=f.get, reverse=True)
    return j[:k]

print(topKList([1,1,1,2,2,3], 2))


def topKList(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

#     freq = []
#   for _ in range(len(nums) + 1):
#     freq.append([])

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print(topKList([1,1,1,2,2,3], 2))