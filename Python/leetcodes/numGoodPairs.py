nums = [1,2,3,1,1,3]

def IdenticalPairs():
    used = {}
    totalpairs = 0
    for i in nums:
        if i in used:
            totalpairs += used[i]
            used[i] += 1
        else:
            used[i] = 1
    return(totalpairs)
           