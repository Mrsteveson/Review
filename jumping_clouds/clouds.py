def jumpingOnClouds(c):
  # Planning phase 
  jumps = 0
  current = 0
  # keep track of where our finish line is 
  finish = len(c) - 1
  # while loop through c 
  # what's the while loop criteria? 
  while current < finish:
    # stop ourselves from overshooting past the bounds of the array 
    if current + 1 == finish or current + 2 == finish:
      return jumps + 1
    # keep track of i+1 and i+2 to see if we can double jump or not 
    # if we can't double jump, do a single jump 
    # if we can't do a single jump, don't jump 
    elif c[current + 2] == 0:
      # double jump 
      # how do we double jump? 
      # a double jump would have us increment i twice 
      current += 2
      # we can't do that with a for loop 
      # increment jump counter 
      jumps += 1
    # else do a normal jump 
    else:
      current += 1
      # increment jump counter 
      jumps += 1
​
  # return jump counter
  return jumps