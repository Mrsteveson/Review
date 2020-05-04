def freqQuery(queries): 
  # we'll use a dict to store the data 
  # actual data will be the keys, values will be the counts of how many 
  # times the data has shown up 
  # we'll use another dict to store the frequencies of frequencies (freqOfFreqs)
  # keys will be the number of times each data has shown up in the first dict
  # values will the number of times those frequencies show up 
​
  # for query in queries
    # if query[0] == 1:
      # perform the insert operation with query[1]
      # increment the count of query[1] in our dict if it exists 
      # if it doesn't exist, add query[1] as a key to our dict with a 
      # count of 1 
      # decrement the old value in our freqOfFreqs for the corresponding freq
      # increment the new value in our freqOfFreqs for the corresponding freq
    # if query[0] == 2:
      # delete query[1] from our data structure (if it exists)
      # decrement the count of query[1] in our dict if it exists
      # if it doesn't exist, don't do anything 
      # decrement the old value in our freqOfFreqs for the corresponding freq
      # increment the new value in our freqOfFreqs for the corresponding freq
    # if query[0] == 3:
      # now that we're using a second dict to keep track of frequencies of 
      # frequencies, we can lookup query[1] in our second dict to see if 
      # it has a value > 0
      # if yes, push a 1 to our answers array 
      # it not, push a 0 to our answers array 
​
​
​
      # check if any element in our data structure shows up query[1] times 
      # let's say we are using a dictionary to store our data 
      # check each key-value pair in our dict and see if any of the values 
      # match query[1] 
      # if yes, push a 1 to our answers array 
      # if not, push a 0 to our answers array 
      # as soon as we find a match for query[1], break out of the loop


# defaultdict is the same as normal dictionaries, except a defaultdict
# sets a default value if a key has not been set yet; this is mostly
# for convenience 
from collections import defaultdict
​
def freqQuery(queries):
  val_counts = defaultdict(int)
  freq_counts = defaultdict(int)
  answers = []
​
  for i, j in queries:
    if i == 1:
      # O(1)
      if j in val_counts:
        # decrement the value's old count 
        if freq_counts[val_counts[j]] > 0:
            freq_counts[val_counts[j]] -= 1
        val_counts[j] += 1
        # increment the frequency in freq_counts 
        freq_counts[val_counts[j]] += 1
      else:
        val_counts[j] = 1
        if freq_counts[val_counts[j]]:
          freq_counts[val_counts[j]] += 1
        else:
          freq_counts[val_counts[j]] = 1
    if i == 2:
        # O(1)
        # check that the value exists in val_counts
        if val_counts[j]:
          # decrement the old frequency count 
          freq_counts[val_counts[j]] -= 1
          val_counts[j] -= 1
          # increment the new frequency count 
          freq_counts[val_counts[j]] += 1
    if i == 3:
      # O(n) linear in the number of key, value pairs 
      # aim for a O(1) runtime 
      # somehow check j in an object 
      # instead of having the j values be checked against 
      # the values in an object, it would be much faster 
      # to check the j values against the keys of an object
      if j in freq_counts and freq_counts[j] > 0:
        answers.append(1)
      else:
        answers.append(0)
      
  return answers
