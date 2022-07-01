def lengthOfLongestSubstring(s):
    dict = {}
    start = maxsublength = 0
    for i, c in enumerate(s):
        if c in dict and start <= dict[c]:
            start = dict[c] + 1
        else:
            maxsublength = max(maxsublength, i - start + 1)
        dict[c] = i
    return maxsublength
        

print(lengthOfLongestSubstring("dvdf"))

