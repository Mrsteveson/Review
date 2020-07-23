def biggerIsGreater(w):
    min_diff = float("inf")
    smallest_letter_index = 0
    chars = list(w)
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # traverse the string right to left
    for i in reversed(range(1, len(chars))): 
        # compare the current letter to the letter to the left of the current 
        # if the letter to the left of the current is smaller 
        if chars[i] > chars[i-1]:
            # we need to swap the left character with another 
            # loop over all characters to the right 
            for j in range(i, len(chars)):
                # subtract current character from 
                diff = ord(chars[j]) - ord(chars[i-1])
                if diff > 0 and diff < min_diff:
                    min_diff = ord(chars[j]) - ord(chars[i-1])
                    smallest_letter_index = j
            chars[i-1], chars[smallest_letter_index] = chars[smallest_letter_index], chars[i-1]
            # sort the rest of the characters after the swapped character 
            return "".join(chars[:i] + sorted(chars[i:]))
​
    return "no answer"
​
    # how do we handle pairs where the left character needs to be swapped 
    # but the character to swap it with is not a character adjacent to it?
​
    # one way to figure out the smallest larger character to replace by is to 
    # find the character in the string with the smallest positive difference 
    # find the smallest positive unicode difference between the character to
    # replace and any other character in the string 
​
    # Given a string like "dkhc"
    # "d" is the character that we need to replace since all of the other 
    # characters in the string are ordered in descending order 
    # it doesn't suffice to just swap "k" and "d" since the smallest larger
    # character in the string is "h"
    # so we need to replace "d" with "h"
    # then put the other characters in lexicographically sorted order after "h"

def bigger_is_greater(w):
	# turn the input string into a list of chars
	chars = list(w)
	# index for when we traverse the list from right to left
	# in order to find the char that needs to be swapped
	i = len(chars) - 1
	# loop through the list until we find the char to swap
	while i > 0 and chars[i-1] >= chars[i]:
		i -= 1
	# if i gets all the way to the left of the array, then we 
	# didn't find a char that needs to be swapped out
	if i <= 0:
		return "no answer"
	
	# once we've found the char to swap, perform another traversal
	# starting from the right of the list to the left in order to 
	# find the smallest char that is greater than the char that 
	# needs to be swapped
	while chars[j] <= chars[i-1]:
		j -= 1
	# at this point, j is pointing at the smallest char that is 
	# greater than the char that needs to be swapped
	# swap them 
	chars[i-1], chars[j] = chars[j], chars[i-1]
	
	# now we need to change the string so that every char to the 
	# right of the swapped char is sorted in lexicographical order
	# it turns out we don't need to perform a full-on sort here
	# because it turns out that any chars we didn't swap are 
	# already in descending lexicographical order 
	# so, instead of performing a full-on sort, all we need to
	# do is reverse the sub-list starting at the char directly
	# to the right of the swapped char
	chars[i:] = chars[len(chars)-1 : i-1 : -1]
	
	# finally, join the list of chars back into a string
	return "".join(chars)