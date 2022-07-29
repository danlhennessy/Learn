import re
print('\tTab')
print(r'\tTab')

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
charset = re.compile(r'[-.]')  # character set of only . or -

  
f = open(r'fundamentals\Built In Modules\regex\data.txt', 'r')
contents = f.read()
pattern = re.compile(r'(\d\d\d)[-.]\d\d\d[-.]\d\d\d\d')  # Match digits and dots/dashes in specific format, e.g: 178-555-4899
matches = pattern.finditer(contents) # finditer provides an iterable object if there is a match. Otherwise it returns None
list_ofmatches = pattern.findall(contents)
firstmatch = pattern.search(contents)
    
for match in matches:
    print(match, match.group(1))  # Group(1) is the first group defined in the compile section for pattern
    
print(firstmatch)