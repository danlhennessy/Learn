def isPalindrome(x):
        xstring = str(x)
        if x < 0:
            return False
        #Slice 'xstring' and move from end backwards, 1 step at a time
        elif xstring[::-1] == xstring:
            return True
        else:
            return False

print(isPalindrome(567))

print(isPalindrome(565))