def smallest_missing(arr):
  # how do we know that the first missing element is 0? 
  # how do we find the sequence? 
  # what's the definition of "missing"? 
​
  # yes, the sequence will always increase by 1 
​
  # Idea 1: 
  # given that the array is already sorted, can we check if the 
  # next array element == the current array element + 1? 
  # if not, then we know that there's the missing element
  # looks like we can assume that 0 is always the smallest missing 
  # number; if we don't see a 0 at the beginning, that's our
  # missing number 
​
  # Idea 2a:
  # O(n) 
  # Worst case is when everything is in order 
  # loop through the array using array indices 
  for i in range(len(arr)):
    # check that each array element matches its index 
    if arr[i] != i: 
      # if it doesn't, return i as our smallest missing element 
      return i 
  # return the length of the array if we reach the end of the loop 
  return len(arr)
  # What's the smallest index in the array where its value doesn't 
  # match the index? 
​
  # Idea 2b: 
  # can we take advantage of the fact that the array is already 
  # sorted to perform this more efficiently? 
  # Do we need to check every single array element for us to still 
  # figure out the correct answer? 
  # We need to check every array element to make sure it matches 
  # its corresponding index 
  # Can we utilize binary search for this? 
    # the array needs to already be sorted 
    # find the midpoint of our array 
​
print(smallest_missing([0, 1, 2, 6, 9, 11, 15]))
print(smallest_missing([1, 2, 3, 4, 6, 9, 11, 15]))
print(smallest_missing([0, 1, 2, 3, 4, 5, 6]))
print(smallest_missing([])) # should return 0 