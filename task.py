
 

 
nums = [1, 5, 2, 1, 4, 5, 1]
 
dup = {x for x in nums if nums.count(x) > 1}
print(dup)  # {1, 5}

def duble(data):
    return list(filter(lambda x: data.count(x) > 1, data))

print(duble(nums))