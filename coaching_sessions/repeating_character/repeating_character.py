# notes for firstNotRepeatingCharacter problem
def firstNotRepeatingCharacter(s):
    # O(n) + O(n) == O(2*n)
    # create a dictionary to save all the chars in the string as keys
    # with the values as how many times that character shows up in the 
    # input string 
    # dictionary entries are not ordered 
    # instead of looping through the dictionary entries 
    # we can loop through the input string again
    # for each character, access that character's value to check
    # how many times it showed up
    # do this until we find a key value pair whose value == 1
    # return that character 
    # if we don't find an entry in the dictionary where value == 1, 
    # then return '_'
​
# Incomplete notes for rotateImage problem
def rotateImage(a):
    # get the length of one of the inner arrays 
    # the length of an inner array will match the number 
    # of arrays in the outer array 
    
    # pattern: outer elements swap and reflect their coordinates
    # as we move "in", inner elements do the same thing 
​
    # using additional memory: create another n x n matrix 
    # for each element with coordinates i and j
    
def first_not_repeating_character(s):
	counts = {}
    
    for c in s:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
​
    for c in s:
        if counts[c] == 1:
            return c
​
    return '_