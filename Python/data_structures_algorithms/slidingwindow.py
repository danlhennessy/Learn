#Example: Given an list of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the list.

def maxSum(lst, k):
    # length of the list
    n = len(lst)
  
    # n must be greater than k
    if n < k:
        print("Invalid")
        return -1
  
    # Compute sum of first window of size k
    window_sum = sum(lst[:k])
  
    # first sum available
    max_sum = window_sum
  
    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        window_sum = window_sum - lst[i] + lst[i + k]
        max_sum = max(window_sum, max_sum)
  
    return max_sum
  
  
# Driver code
lst = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(lst, k))