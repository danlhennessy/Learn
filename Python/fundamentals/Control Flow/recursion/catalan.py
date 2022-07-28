# Count the number of unique expressions containing n pairs of parentheses which are correctly matched. 
# For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

catalan_nums = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
# Relationship: Cn = 2n! / ((n+1)!n!)
# n = 1:   2! / 2!1! = 2/2 = 1
# n = 2:   4! / 3!2! = 24/12 = 2