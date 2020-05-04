def containsDuplicates(a):
    # O(n log n) runtime, O(1) space
    # sort the array 
    # all duplicates will now be next to each other
    # iterate through the array and check the i + 1 element 
    # to see if it matches the current element 
​
    # O(n) runtime, O(n) space
    # iterate through the array elements 
    # save elements in a hashmap that has the element as the key 
    # and the counts as values 
    # as soon as we see a duplicate, return true 
    # as soon as we see an element in our hashmap that we've already 
    # added, then that's a duplicate 
​
    # O(n) runtime, O(n) space
    # variant of the hashmap idea above, but use a set data structure
    # instead 
    # sets are slightly more appropriate in this case, since we only
    # care about whether we've added the element to the set already;
    # we don't really need values for that 
    # iterate through our array 
    # check if the current array element is in the set 
    # if it isn't, then we haven't seen it before
    # add it to the set 
    # if it's already in the set, then we've seen it before
    # return true 
    # if we get through the whole array without seeing duplicates in
    # the set, return false 
​
    # O(n^2) runtime, O(1) space 
    # use python's built-in list.count()
    # iterate through the array
        # call list.count() on the current element 
        # if the list.count() call returns more than 1 
        # then return true 