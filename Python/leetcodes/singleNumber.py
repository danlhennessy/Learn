def singleNumber(nums):
    for i in nums:
        if nums.count(i) != 2:
            return(i)
        
print(singleNumber([7,6,6,2,2,7,9]))