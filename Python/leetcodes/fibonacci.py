#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    print(a)
    return(a)

climbStairs(7)

#Multiple assignment:
#a, b = 0, 1

# a, b = b, a+b

# Is Equivalent to:

# temp = a
# a = b
# b += temp