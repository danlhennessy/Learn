nums = [3,1,2,10,1]

def runningSum(mylist):
    sum = 0
    ans_list = list()
    for index in nums:
        sum += index 
        ans_list.append(sum)
    return(ans_list)
print(runningSum(nums))
