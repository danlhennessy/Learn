#Given a string s, find the length of the longest substring without repeating characters.



def lengthOfLongestSubstring(s):
        x = 0
        maxlen = 0
        while s[x:]:
            longword = []
            temp = 0
            for v in s[x:]: #Find the longest string of nonrepeating characters starting at each letter
                if v in longword:
                    break
                else:
                    longword.append(v)
                    temp += 1
                    if temp > maxlen:
                        maxlen = temp
            x += 1 # Adding 1 to x removes the first letter of the string, the loop starts again and finds the longest nonrepeating substring from the new first letter
        return(maxlen)       
        

print(lengthOfLongestSubstring("pwwkew"))