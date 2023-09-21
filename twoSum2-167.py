def towSums(arr , target):
    prev = {}
    new_numbers = sorted(arr)
    print(new_numbers)

    for i, val in enumerate(new_numbers):
        diff = target - val
        if diff in prev:
            return [prev[diff] + 1 , i + 1]
        prev[val] = i   


print(towSums([2,7,11,15], 9))  