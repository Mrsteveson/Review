def sumOfTwo(a, b, v):
    # examples are sorted, but are we going to actually get sorted input? 
    # no, input arrays may not be sorted 
​
    # sort the two arrays 
    # could we use a similar two pointer strategy? 
​
    # if we're hash tables, what is going in the hash tables? 
    # store the elements of one of the arrays in the hash table 
    # make a sum of an element from a and an element from b 
    # check if they equal v 
    # does moving all of the elements from one array into a hash table help us? 
    # hash tables help us with lookups 
    # loop through each element x in b
        # check if v - x is in the hash table 
        # as soon as we see that some v - x is in the table 
        # then we've found a pair 
        # return true 
    # no pair was found, return false 
​
​
# alternative strategy that utilizes a hash table 
​
# can we consider a "easier" problem? 
# if we only had a single array and had to find two values in it 
# that summed up to v, how would we do that? 


def sum_of_two(arr, v):
    # sort the input array 
    # use the 2 pointer technique:
    # init one pointer at the start of the array 
    # init another pointer at the end of the array 
    # would we ever allow the two pointers to pass each other? 
    # if the pointers pass each other, then we'd just be considering 
    # two values we've already looked at; we shouldn't see a new combo 
    # by having the pointers pass each other 
    # break out of the loop if the pointers pass each other 
    # there's no two numbers that sum up to v 
    # if sum of both pointers == v
        # return 
    # check if the sum of both pointers == v 
        # if the sum of both pointers < v 
            # then that means we need a larger sum 
            # increment the left pointer 
        # if the sum of both pointers > v 
            # then that means we need a smaller sum 
            # decrement the right pointer 