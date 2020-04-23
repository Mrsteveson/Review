def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	# go with what we already know off the bat from the problem statement 
	# we're working with anagrams: a word formed from another by rearranging its letters 
	# the output needs to be in the form of an array of arrays 
	# we need to be able to tell if two words are anagrams 
	# we're working with strings 
​
	# work through the given examples with pencil and paper (or whatever scratch medium you
	# like using)
	# also expand on given examples or create new ones and work through them to broader and 
	# reinforce your own understanding of the problem 
​
	# what data structure should we use to hold our groupings? 
	# linked list since we're working with a group of arrays
	# expected output type is array of arrays 
	# would that be a suitable data structure for us to use? 
	# if we're using an array of arrays: for the current word, sort it and check it against the 
	# sorted version of the latest word in each group 
	# using an array of arrays, we end up performing more sorts than we need to 
	# idea: in order to reduce the number of redundant sorts, let's save the sorted version of 
	# each word and associate it with its grouping 
	# because we want to keep track of the association between the sorted word and its grouping, 
	# use a dictionary with the sorted word as key and array of words as value 
​
	# how do we determine if two words are anagrams? 
	# 1. if two words, after they are sorted, exhibit the same letters in the same order 
	# 2. use dictionaries to store the letters of one of the strings as keys with values as counts 
	# of each letter; go through the other string, decrementing the letter in the dictionary's count
	# until we see that either the two words are not anagrams or they are 
​
	# how do we take our dictionary and convert it into the expected output type? 
	# return the values of our dictionary using dict.values()

def groupAnagrams(strs):
        hash = {}
        for i in strs:
            key = ''.join(sorted(i))
            if hash.get(key):
                hash[key].append(i)
            else:
                hash[key] = [i]
        return hash.values() 