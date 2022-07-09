mylist = [1,7,6,4,9,3,4,5]
def findarea():
    n = 0
    maxarea = 0
    for i, v1 in enumerate(mylist):
        rollingarea = 0
        width = 0
        n += 1
        print(f"Starting from {n - 1} index")
        for i, v2 in enumerate(mylist[n:]):
            width += 1
            rollingarea = min(v1, v2) * width
            print(rollingarea)
            if rollingarea > maxarea:
                maxarea = rollingarea
    return maxarea

print(findarea())