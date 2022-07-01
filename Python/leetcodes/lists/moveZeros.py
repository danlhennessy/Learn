def moveZeroes(nums):
    for i in nums:
        if i == 0:
            nums.append(nums.pop(nums.index(i)))
    print(nums)
    
nums = [0,3,4,0,6,7]

moveZeroes(nums)