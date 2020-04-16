def groupingDishes(dishes):
    # Use a hash table to store dishes as keys and values as the ingredients
    # How does that help us?
​
    # The expected output makes me think that we might want to end up with
    # ingredients as keys with dishes they belong in as values
​
    # if we go with ingredients as keys and dishes as values, how do we 
    # produce that given our dishes array as input?
​
    """
    {
        "Cheese": ["Quesadilla", "Sandwich"],
        "Salad": ["Salad", "Sandwich"],
        "Sauce": ["Pizza", "Quesadilla", "Salad"],
        "Tomato": ["Pizza", "Salad", "Sandwich"]
    }
    """
​
    # loop through each dish array
        # loop through the ingredients, skipping the first array element
            # check if the ingredient is a key in our hash
                # add it if it isn't
            # push the dish into a list at hash[ingredient]
​
    # at this point, we'll have our dict containing all of the ingredients
    # with their corresponding dishes
    # at this point, we need to make sure every list of dishes is sorted 
​
    # loop through every key-value pair in the hash
        # check if the ingredients list's length > 1
            # if it is, sort it
            # else, remove the key-value pair
​
    # now we need to convert the data in the hash to an array of arrays 
    # take the keys from our hash and create a new array with the key 
    # as the first element, followed by all of the key's dishes in the array
    # now we need to make sure that the lists are sorted by their first 
    # array elements
    # use the built in sort method to do that with a lambda/callback function
​
    # return the list of lists
	
​
def areFollowingPatterns(strings, patterns):
    # should the patterns to be keys, or the strings to keys?
    # if we have patterns as keys:
​
    # if an element in the patterns array is already in the hash
    # then we know we want to return False when we see that we're
    # overwriting the value 
​
    # loop through both strings and patterns arrays in unison 
        # check if the pattern elem is in the hash 
        # if it isn't, add it as a key with its value as the corresponding
        # element in the string array 
        # if it is, check if the elem in the strings array matches the 
        # key's current value 
        # if it doesn't, then the pattern doesn't match 
​
    # also have to check the other "direction", i.e. strings to patterns 
    # repeat the above step but with strings as keys and patterns as values 
​
    # use a set to check for duplicate strings in the strings array 
    # compare the length of the set with the length of our hash table 
​
    """
    {
        "a": "cat",
        "b": "dog",
    }
    """