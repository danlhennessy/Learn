
list = [1,2,3,4,5,6,7,8,24,25,26,27,28,34,35,36,37,38,45,46,47,48,49]

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

#List must be sorted for binary seach to work

def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
    if high < low:
        return -1
    
    midpoint = (low + high) // 2
    
    if list[midpoint] == target:
        return midpoint
    if target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else: # target > list[midpoint]
        return binary_search(list, target, midpoint+1, high)
    
if __name__=='__main__':
    list = [1,2,3,4,5,6,7,8,24,25,26,27,28,34,35,36,37,38,45,46,47,48,49]
    target = 6
    print(naive_search(list, target))
    print(binary_search(list, target))