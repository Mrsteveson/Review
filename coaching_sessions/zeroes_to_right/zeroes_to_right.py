# O(n^2)
# what's the best we could do this in? O(n)
def zeros_to_right(arr):
  # var to keep track of non-zeros 
  n_zeros = 0
  # iterate through array 
  # counting number of zeros 
  for x in arr:
    if x == 0:
      n_zeros += 1
​
  # worst case, we have an array of all 0s or a lot of 0s 
  for x in arr:
    # if we see a zero 
    if x == 0:
      # remove it 
      # O(n)
      # could we swap it instead? 
​
      arr.remove(x)
      arr.append(0)
​
  print(arr) 
  return len(arr) - n_zeros
​
def zeros_to_right(arr):
  # have a left pointer that stops on 0s 
  # have a right pointer that stops on non-0s 
​
  # traverse both pointers towards each other 
    # if left is on a non-0, increment it 
      # increment our non-zeros counter 
    # if right is on a 0, decrement it 
    # when left is pointing at a 0 and when right is pointing
    # at a non-0
      # swap their respective values 
      # move both pointers towards each other 
​
arr3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print(zeros_to_right(arr3))
​
arr1 = [0, 3, 1, 0, -2]
print(zeros_to_right(arr1))
​
arr2 = [4, 2, 1, 5]
print(zeros_to_right(arr2))