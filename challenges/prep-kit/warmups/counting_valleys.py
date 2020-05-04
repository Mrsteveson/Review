def countingValleys(n, s):
  height = 0
  valleys = 0

  for step in s:
    if step == 'U':
      height += 1
      if height == 0:
        valleys += 1
    else:
      height -= 1

  return valleys