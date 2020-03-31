def freqQuery(queries): 
  # we know we're interested in knowing the frequency of elements 
  # order doesn't matter, since for the frequency query, we don't 
  # care about the order of the elements, we just want to know 
  # how many times each shows up 
  # is an array well-suited to handle this use-case?
  # dicts/hashmaps/objects are a lot better suited to keeping track of 
  # frequencies 
  # use a dictionary to keep track of the data as keys and their frequencies
  # as values
  # init an output array
​
  # O(n) for the loop, so overall worst-case is O(n^2) due to the 3
  # for loop through all the queries 
    # checks for each query type 
    # if query[0] == 1: O(1)
      # increment the data if it exists in the dict
      # init the data to a freq of 1 if it doesn't exist in the dict
    # if query[0] == 2: O(1)
      # decrement the data if it exists in the dict
      # do nothing if the data isn't in the dict
    # if query[0] == 3
      # why is this operation expensive? 
      # dicts aren't great at looking up values
      # we need some way to make looking up values efficient
      # preferably with the stipulation that whatever we do to improve 
      # the efficiency of looking up values doesn't adversely affect 
      # the other operations 
​
      # could we sort the values in the dict? O(n log n)
      # we'd be able to look up the values quickly if they were keys 
      # in another dict; what would be the format of this dict? 
      # values from the first dict would be keys, what would the values 
      # of this second dict be? 
      # the values in this second dict will be the frequency of the frequencies
      # from the first dict 
​
      # O(n) since we don't have efficient lookup on values 
      # so if we want to look through all the values to find one that 
      # matches what we're looking for, it's a linear operation since 
      # the values need to be dumped into an array and looped through 
      # to see if any of them match
​
      # look through all of the values of our dict to find if any of them
      # match the frequency we're looking for 
      # if we find it, add a 1 to our output array
      # if we don't find it, add a 0 to our output array
  
  # return our output array
​
    # a plan that improves on the overall runtime without adversely affecting
    # queries 1 and 2 
    # for loop through queries: O(n)
      # if query[0] == 1: O(1)
        # decrement the value of the old freq in the second dict
        # increment the data if it exists in the first dict
        # init the data to a freq of 1 if it doesn't exist in the first dict
        # increment the value of the new freq in the second dict if it exists 
        # init the freq in the second dict to 1 if it doesn't 
      # if query[0] == 2: O(1)
        # decrement the value of the old freq in the second dict
        # decrement the data if it exists in the dict
        # do nothing if the data isn't in the dict
        # increment the value of the new freq in the second dict if it exists 
        # init the freq in the second dict to 1 if it doesn't exist
      # if query == 3: O(1)
        # check if the second dict has query[1] as a key and if its value > 0
          # add a 1 to our output array
        # otherwise
          # add a 0 to our output array