def kidsWithCandies(candies, extraCandies):
    result = []
    for i in candies:
        if i + extraCandies >= max(candies):
            result.append(True)
        else:
            result.append(False)
    return(result)
            
kidsWithCandies([2,3,5,1,3], 3)


#Testing....
testlist = []

testlist.append(True)
testlist.append(True)
testlist.append(False)

print(testlist)