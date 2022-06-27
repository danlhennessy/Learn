#Two strings are anagrams if you can make one from the other by rearranging the letters.

#Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

def is_anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

print(is_anagram("dog", "god"))
