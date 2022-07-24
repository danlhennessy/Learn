ansseq = [1,4,7,10,13,16]

def getnuminseq(idx):
    if idx <= 0:
        return 1
    return (getnuminseq(idx - 1) + 3)

print(getnuminseq(2))