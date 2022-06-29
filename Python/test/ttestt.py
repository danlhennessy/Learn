#print(dir(int))



def format_number(num):
    backstring = (str(num))[::-1]
    result = ""
    count = 0
    for v in backstring:
        if count == 2:
            result += ","
            count = -1
        count += 1
    return result[::-1]

print((format_number(1028000)))