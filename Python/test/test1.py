mynums = [1,11,3,0,15,5,2,4,10,7,12,6]


def largestrange(nums):
    sortedlist = sorted(nums)
    last = sortedlist[0]
    cursub = [last]
    longestsub = []
    for i, v in enumerate(sortedlist[1:]):
        print(f'trying {v}')
        if v == last + 1:
            cursub += [v]
            last = v
            if len(cursub) > len(longestsub):
                longestsub = cursub
        else:
            cursub = [v]
        print(cursub)
            
    print([longestsub[0], longestsub[-1]])
    
largestrange(mynums)