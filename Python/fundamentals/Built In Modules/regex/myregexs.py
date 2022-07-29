import re

string = '''sdfsdfdsfds
danh118@gmail.com
www.google.com
fel123
'''

email_pattern = re.compile(r'\w+@\w+\.\w+')

list_ofmatches = email_pattern.findall(string)
print(list_ofmatches)