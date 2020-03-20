def climbingStaircase(n, k):
    answer = []
​
    if n < 0:
        return answer
    if n == 0:
        answer.append([])
        return answer
​
    for i in range(1, k + 1):
        for seq in climbingStaircase(n - i, k):
            answer.append([i] + seq)
​
    return answer

# Variant of the staircase problem that wants us to return 
# the number of ways in which we can reach n steps using 1,
# 2, or 3 jumps
def stepPermsRecurse(n, cache):
    # check the cache to see if n is already an answer we've solved before
    if cache[n] > 0:
        return cache[n]
    # base cases 
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        # otherwise, recurse, saving the answer to the cache 
        cache[n] = stepPermsRecurse(n-1, cache) + stepPermsRecurse(n-2, cache) + stepPermsRecurse(n-3, cache)
        return cache[n]
​
# Complete the stepPerms function below.
def stepPerms(n):
    # set up the cache to save pre-calculated answers 
    cache = [0 for _ in range(n + 1)]
    return stepPermsRecurse(n, cache)
​
​
​
# Variant of the staircase problem that wants us to return the 
# actual sequences of jumps to reach n steps, with at most k
# jumps at one time
def climbingStaircase(n, k):
    # differences with eating cookies 
    # 1. with this problem, the number of stairs that can be jumped is an 
    # arbitrary input parameter 
    # 2. we want to actually calculate the sequences of jumps, not just figure 
    # out how many sequences there are 
    # we'll end up returning an answer array whose length of would be equal to 
    # the answer we'd get from the eating problems 
    
    answer = []
​
    # base case(s)
    if n <= 0:
        answer.append([])
        return answer
    if n == 1 and k > 0:
        answer.append([1])
        return answer
​
    # what goes in as parameters to the recursive call?
    # call the recursive function in a loop up to whatever k is
    # k + 1 in the range call to include k itself
    for i in range(1, k + 1):
        # getting a bunch of nested arrays that we don't want
        # also not getting any numbers in the lists other than 1
        for seq in climbingStaircase(n - i, k):
            # append the other k values to the arrays returned by the recursive calls
            answer.append([i] + seq)
​
    return answer