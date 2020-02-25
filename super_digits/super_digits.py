# sum the digits of an int in string form 
# return an int
def sum_digits(p):
  l = [] 
  l[:0] = p
  return reduce(lambda x, y: int(x) + int(y), l)
​
def superDigit(n, k):
  # check the length of the string 
  # then check for the terminating case 
  # after the first recursive call, do we still need k? 
  # construct the actual P value by concatenating n k times 
​
  # recursing k times 
​
  # possible base case: 
  # 1. if k <= 0 return 0
  # 2. if P <= 9 (i.e. P is a single digit)
  # 3. check the length of P, but we'd have to transform P into either
  # a string or an array, since we can't take the length of a number 
​
  # repeat this k times: sum the digits of n 
  # recurse so long as P > 9 as a way to check if P has more than 1 digit 
  # if we recurse, then call the function with the sum from the previous 
  # recursion with k = 1
  # in any recursive calls, k will always be 1 
​
  # construct our p 
  # note that it's a string here 
​
  # if len(n) == 1 and k == 1:
  #   return int(n)
​
  p = str(sum_digits(n) * k)
​
  if len(p) < 2:
    return int(p)
​
  # call our sum_digits function 
  # this will update p to be an integer 
  # p = sum_digits(p)
​
  return superDigit(p, 1)
​
  # use the same function signature 
  # if we aren't in the base case, then P > 9 
  # sum the digits together 
  # how should we sum the digits together?