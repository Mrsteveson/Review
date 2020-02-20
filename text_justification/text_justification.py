def text_justification(words, l):
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