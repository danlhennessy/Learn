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
charset = re.compile(r'[-.]')  #  character set of only . or -
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
  # finditer provides an iterable object if there is a match. Otherwise it returns None

f = open(r'fundamentals\Built In Modules\regex\data.txt', 'r')
contents = f.read()
matches = pattern.finditer(contents)
    
for match in matches:
    print(match)