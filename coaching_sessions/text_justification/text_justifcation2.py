def textJustification(words, l):
    # fit as many words from the words array into a line of l characters
    # use spaces to fill in a line if we can't fit words into a line cleanly
    # the spaces need to be evenly distributed between the words in a line
    # if we need to insert an odd number of spaces to fill up a line, put 
    # odd-numbered space in the left slot
    # if we have one word on a line, left justify it with no extra spaces 
    # on the left
​
    # how to think about a strategy at a high level
    # think about how you'd talk about your strategy to someone who 
    # has no idea how to program 
    # _what_ are the steps we're going to take
    # nothing yet about _how_ we're going to do them 
​
    # iterate through the words in the words array 
    # figure out which words go in which lines without worrying about 
    # spacing yet 
    # construct the answer array with the words correctly distributed on
    # each line 
    # keep in mind we need one space after every word except for the last
    # word in the line
​
    # keep track of the current number of chars in the current line 
    n_chars = 0
    answer = []
    line = []
​
    for word in words:
        # if we have chars in the line already, add 1 to account for the spaces between words
        if n_chars > 0:
            n_chars += 1
        # see if the current number of chars in the current line + current
        # word's length + 1 > l
        if n_chars + len(word) > l:
            # if it does, put the current word on the next line 
            # handle justifying this line 
            justified = handle_justification(line, l, n_chars)
            # add this line to our answer array
            answer.append(justified)
            line = []
        else:
            # otherwise add it to the current line and continue on
            line.append(word + " ")
            n_chars += len(word)
​
    # special handling for the last line 
    # add any additional spaces to the end of the line 
    if len(line) > 0:
        # turn the contents of the last line into a string so we can add spaces to it 
        string = " ".join(line)
        # add spaces to the end until the total length of the line reaches l
        string += (" " * (l - len(string)))
        answer.append(string)
​
    return answer
        
def handle_justification(line, l, n_chars):
    # figure out how much space padding each line needs and insert the 
    # necessary number of spaces in the correct distribution
    n_words = 0
    for word in line:
        n_words += 1
    # "This is an" => "This    is    an"
    # figure out length of current line 
    # l - length of the current line = number of spaces we need to insert 
    spaces_to_insert = l - n_chars
    # number of spaces to insert / how many spaces are in the line so that we know 
    # how many extra spaces to put in each space 
    padding_per_space = spaces_to_insert / (n_words - 1)
    # add any remaining spaces left over starting from the leftmost space, going right
    leftover_spaces = spaces_to_insert % (n_words - 1)
    # take the leftoever spaces and start adding them one by one starting with the leftmost space


def textJustification(words, l):
    output = []
    line = []
    n_chars = 0
​
    for word in words:
        # add a space to n_chars only if we already have at least one word
        # this accommodates us adding a space for the last word in the line
        if n_chars > 0:
            n_chars += 1
​
        n_chars += len(word)
​
        # once we've overshot the length limit, add the current line to our result
        # and reset our current line and counter
        if n_chars > l:
            justified = handle_justification(line, l)
            output.append(justified)
            n_chars = len(word)
            line = []
        
        line.append(word)
​
    # special handling for the last line after we've iterated through all the words
    # turn the line into a string and then add any additional spaces we need
    if len(line) > 0:
        string = " ".join(line)
        string += (" " * (l - len(string)))
        output.append(string)
​
    return output
​
​
def handle_justification(line, l):
    output = ""
​
    # get total number of chars in the line
    n_chars = 0
    for w in line:
        n_chars += len(w)
​
    # extra spaces are the number of spaces we need to add on top of the spaces
    # that should already be in the line
    extra_spaces = l - n_chars
    # number of spaces that should already exist in the line
    normal_spaces = len(line) - 1
​
    # if there are no normal spaces in this line, then that means there is only
    # one word in the line; add all of the extra spaces after the word
    if normal_spaces == 0:
        return line[0] + (" " * extra_spaces)
​
    # padding is the number of spaces we need to add to every normal space to distribute
    # then evenly
    padding = extra_spaces // normal_spaces
    # remainder is any remaining spaces we need that don't evenly divide the number of
    # normal spaces
    remainder = extra_spaces % normal_spaces
​
    # for each word in the line, add on the number of spaces needed to evenly distribute
    # all of the spaces between every word
    for i, word in enumerate(line):
        spaces = padding
        
        # add on any remaining spaces we need to reach the length limit
        if i < remainder:
            spaces += 1
        
        # if this is the last word in the line, don't add any spaces to it
        if i == len(line) - 1:
            spaces = 0
​
        spaces = " " * spaces
        output += (word + spaces)
​
    return output