#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

#Works except if there are any 9s:
#def plusOne(digits1):
    #digits1[-1] += 1
    #return digits1

def plusOne(digits):
    largestr = ""
    for v in digits:
        largestr += str(v)
    largeint = int(largestr) + 1
    largestr = str(largeint)
    return([v for v in largestr])

print(plusOne([1,2,3]))