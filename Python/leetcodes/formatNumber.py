def format_number(num):
    backstring = (str(num))[::-1]
    result = ""
    count = 0
    for i, v in enumerate(backstring):
        result += v
        if i < len(backstring) - 1:
            if count == 2:
                result += ","
                count = -1
        count += 1
    return result[::-1]

print((format_number(128000)))