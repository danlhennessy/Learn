#Given an array of integers nums, calculate the pivot index of this array.

#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

#If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

#Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums):
    listsum = sum(nums)
    rollingsum = 0
    for i, v in enumerate(nums):
        if rollingsum == (listsum - v) // 2:
            return i
        elif rollingsum > (listsum - v) // 2:
            return -1
        else:
            rollingsum += v

nums = [-1,-1,-1,-1,-1,0]
print(pivotIndex(nums))
