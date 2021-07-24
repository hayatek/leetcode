nums = [0,1,2,2,3,0,4,2]
val = 2

num_len = len(nums)
del_count = 0
k = 0

for i in range(num_len):
    if nums[i] == val:
        nums.append(val)
        del_count += 1

print('a nums=',nums)

for i in reversed(range(num_len)):
    if nums[i] == val:
        del nums[i]

k = num_len - del_count
print('k=',k)
print('nums=',nums)