digits_to_letters = {
  0: '0',
  1: '1',
  2: 'ABC',
  3: 'DEF',
  4: 'GHI',
  5: 'JKL',
  6: 'MNO',
  7: 'PQRS',
  8: 'TUV',
  9: 'WXYZ'
}
​
# 987
def telephone_words(digits):
  words = []
​
  # calculate expected output length: l 
  # base case: len(words) == l: return the array 
  # we need to start adding words to our words array 
  # loop over the digits 
    # for the current digit, loop over its letters 
      # call our function recursively with the current letter and the other digits 
        # concatenate the letter to whatever current string we're building up 
        # add the new string to our array 
        # keep doing this until len(words) == l 
​
​
  # 99 
     # WXYZ  
  # 9: WXYZ 4 
  # 8: TUV  3 
  # 7: PQRS 4 
​
  # expected length of output: 
  # output: [WTP WTQ WTR WTS WUP WUQ WUR WUS WVP WVQ WVR WVS ] 4 * 3 * 4 = 48
​
  # try every combination of the letters on the first number with the 
  # letters on the second number and third number 
​
  # do a for/while loop that calls the next number in itself 
  # access 9 to 'WXYZ'
  # loop through WXYZ 
    # telephone_words(W, 87)
      # access 8 to get TUV 
      # loop through TUV 
        # for each letter, call telephone words with WT, 7