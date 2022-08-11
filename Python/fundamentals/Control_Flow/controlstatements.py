#Change sequence of a loop, e.g. returning to the start of a for loop with a Continue statement

for item in 'tent eat tree':
    if item == 'e':
        continue
    print(item)
    
#Break brings the loop to an end

for item in 'tent eat tree':
    if item == 'e':
        break
    print(item)
print('Stopped as there is an e here')

#Pass does nothing, commonly used as a placeholder to prevent script erroring
for item in 'tent eat tree':
    pass