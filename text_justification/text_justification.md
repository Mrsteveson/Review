def text_justification(words, l):
	# what happens if a word's length == l
    # stuff that word in its own line with no spaces on either side 
​
    # can we get words whose length > l? 
    # no, we won't get words with length > l 
	
	# iterate through the array of words 
	# figure out how many words go in the next line 
​
	# figure out how many we can stuff in a single line without going 
	# over the line count 
	# length of current word + 1
	# we need to take into account the spaces we'll need in between words 
​
	# figure out how many spaces we need, as well as how to distribute those spaces
	# number of initial spaces = number of words in this line - 1 
	# number of extra spaces = l - number of characters + number of initial spaces 
	# if there is only one word in this line or we're in the last line 
	# put all extra spaces at the end 
	# if we're not 
	# take number of extra spaces and divide them, starting on the left 
	# between the initial spaces we have 
​
​
​
    # space distributing logic 
    # we need to know how many initial spaces we have
    # so that we know how many we can divide extra spaces into 
    # number of extra spaces we need / number of initial spaces 
    # spaces are only added to the right when there is only one line 
    # in the word or when we're in the last line 
    # we'll need to know when we only have 1 word in a line or if we're 
    # working on the last line