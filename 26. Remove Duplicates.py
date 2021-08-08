nums = [1,1,2]

first_i = 0
for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        nums[first_i+1] = nums[i+1]
        first_i += 1
            
print('k=',first_i+1)
print('outnums=',nums)