class testnum:
    def __init__(self, val):
        self.val = val
    def __sub__(self, other: int):
        return self.val - other
    def __add__(self, other: int):
        return self.val + int(other)
    def __rsub__(self, other: int):
        return other - self.val
        
test1 = testnum(28)
one = test1 - 4
add = test1 + '224'
print(add, one)