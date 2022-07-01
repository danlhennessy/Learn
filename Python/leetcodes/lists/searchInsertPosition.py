# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

nums = [1,3,6,8,9,10]
target = 7
def searchInsert(nums):
    for i,v in enumerate(nums):
        if v >= target:
            return(i)
        elif i == len(nums) - 1:
            return(i+1)
            
print(searchInsert(nums))