nums = [1,2,3,1,1,3]

used = []
totalpairs = 0
n = 0
for i in nums:
    if i in used:
        pass
    else: 
        currentnums = (nums.count(i))
        used.append(i)
        if currentnums > 1:
            
#print(totalpairs)