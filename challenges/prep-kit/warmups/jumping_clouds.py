def jumpingOnClouds(c):
  jumps = 0
  current = 0
  finish = len(c) - 1
 
  while current < finish:
    if current + 1 == finish or current + 2 == finish:
      return jumps + 1

    elif c[current + 2] == 0:
      current += 2
      jumps += 1
    else:
      current += 1
      jumps += 1
​
  return jumps