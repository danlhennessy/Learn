# example facts:
#     m = 3.28 ft
#     ft = 12 in
#     hr = 60 min
#     min = 60 sec
# example queries:
#     2m = ? in --> answer = 78.72
#     13in = ? m --> answer = 0.330
#     13in = ? hr --> answer = ' not convertible!'

"""
Plan:
- Determine both item unit types (distance, weight, time, more?)
- Check if first item type matches 2nd item type (If not, spit out error)
- If items do have the same unit type, then apply a conversion based on a list of ratios (e.g. min to hour = 0.0166667)
- Ratio can be used in either direction (e.g. if min to hour, multiply by ratio, and if hour to min, divide by ratio)
"""

distances = ['m', 'ft']
times = ['hr', 'min']

ft_m_ratio = 0.3048
min_hr_ratio = 0.0166667

def convert_unit(input):
    if (input[1] in distances and input[2] in distances):
        print('units are both distances')
        if input[1] == 'm':
            return (input[0] / ft_m_ratio)
        else:
            return (input[0] * ft_m_ratio)
    elif (input[1] in times and input[2] in times):
        print('units are both times')
        if input[1] == 'hr':
            return (input[0] / min_hr_ratio)
        else:
            return (input[0] * min_hr_ratio)
    else:
        print('Not Convertible!')


print(convert_unit((4, 'ft', 'm')))