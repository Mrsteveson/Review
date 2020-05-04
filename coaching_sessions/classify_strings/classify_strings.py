def classifyStrings(s):
    # not counting y as a vowel 
    # bad: 3 consecutive vowels or 5 consecutive consonants 
    # mixed: can be both due to a ? character 
    # good: everything else 
​
    # must mixed strings have ?s?
​
    # regexes as a way to solve this
    # we're going to need some way to differentiate vowels and consonants
    # one way we could differentiate vowels and consonants is to have a set of 
    # vowels; if the current char is in the set, it's a vowel, otherwise it's 
    # a consonant 
​
    # for each char in the input string 
        # check from the current char up through current + 3 to see if all those 
        # chars are vowels 
        # check from the current char up through current + 5 to see if all those 
        # chars are consonants
        # what to do if we encounter a ? char
​
    # have a counter that keeps track of the current run of vowels/consonants
    # have a boolean toggle to indicate whether we're keeping track of vowels
    # or consonants 
    # as we're iterating, if we encounter the other type of char, flip the boolean
    # and reset the counter to 1
    # if the boolean is toggled to vowels, then if the counter ever reaches 3, we've 
    # found a run of 3 consecutive vowels
    # if the boolean is toggled to consonants, then if the counter ever reaches 5,
    # we've found a run of 5 consecutive consonants
​
    # ?s are wildcards
    # we should count ?s as both 
​
    # if v >= 3 and c > 0 and c < 5: return "mixed"
    # if c >= 5 and v > 0 and v < 3: return "mixed"
    # v = 3
    # c = 1
    # ?aa 
​
    # answer = "bad"
    # lkhfdtyp?asdf?re
    # v = 0
    # c = 5
​
    # if we encounter the criteria for a bad string, return immediately
    # if we encounter the criteria for a mixed string, save that answer but keep
    # iterating until we reach the end of the string 
    # if we make to the end without ever seeing a mixed or bad string, return "good"
​
    v = 0
    c = 0
​
    vowels = set(['a', 'e', 'i', 'o', 'u'])
​
    if s[0] in vowels:
        v += 1
    elif s[0] == '?':
        v += 1
        c += 1
    else:
        c += 1
    
    answer = "good"
    prev = s[0]
​
    for char in s[1:]:
        # determine whether the char is a vowel or consonant
        if char in vowels:
            v += 1
            if prev not in vowels and prev != '?':
                c = 0
        elif char == '?':
            v += 1
            c += 1
        else:
            c += 1
            if prev in vowels and prev != '?':
                v = 0
​
        if (v >= 3 and c == 0) or (c >= 5 and v == 0):
            return "bad"
        
        if (v >= 3 and c > 0 and c < 5) or (c >= 5 and v > 0 and v < 3):
            answer = "mixed"
​
        prev = char
​
    return answer


"""
This implementation keeps separate counters for vowels, consonants, as well
as additional counters that specifically handle vowels and consonants in
the case we encounter a ? character. In order to get all of the tests to 
pass, we need slightly different logic/handling of the counters, for example,
to correctly handle runs of multiple ?s. 
"""
def classifyStrings(s):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    answer = "good"
	
	# v and c are the "regular" vowel and consonant counters
	# mix_v and mix_c keep track of vowels and consonants when 
	# we encounter a ?
	v, mix_v = 0, 0
    c, mix_c = 0, 0
​
    for char in s:
        # determine whether the char is a vowel or consonant
        if char in vowels:
            v += 1
			# reset counters for the other char type
            c, mix_c = 0, 0
​
        elif char == '?':
			# now that we've seen a ?, switch to using the mixed counters
			# and reset the regular counters so that they're ready if/when
			# we are no longer processing ?s
            mix_v += v + 1
            mix_c += c + 1
            v, c = 0, 0
			
			# check criteria using mixed counters
            if mix_v >= 3:
                c = mix_c
                mix_v = 0
                answer = "mixed"
            elif mix_c >= 5:
                v = mix_v
                mix_c = 0
                answer = "mixed"
​
        else:
            c += 1
			# reset counters for the other char type
            v, mix_v = 0, 0
		
		# check if we have a bad string using the regular counters
        if v >= 3 or c >= 5:
            return "bad"
        
		# check for a mixed string using the mixed counters
        if mix_v + v >= 3 or mix_c + c >= 5:
            answer = "mixed"
​
    return answer