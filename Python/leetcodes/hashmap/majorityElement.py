#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


def majorityElement(nums):
    dict = {}
    halflen = len(nums) * 0.5
    for v in nums:
        if halflen == 0.5:
            return(v)
        if v in dict:
            dict[v] += 1
        else:
            dict[v] = 1
        if dict[v] > halflen:
            return(v)
            
nums = [8,8,7,7,7]
print(majorityElement(nums))