# Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using the 2 x 1 tiles. 
# A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile. 

def uniqueways(n):
    if n <= 2:
        if n < 0:
            return ('number not valid')
        return n
    return uniqueways(n - 1) + uniqueways(n-2)
        
print(uniqueways(1))