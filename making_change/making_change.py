def change(amount, coins):
	# base cases 
	# if there's a negative, we can't make change for that 
	if amount < 0:
	return 0 
	# there's one way to make 0 cents 
	if amount == 0:
	return 1
​
	# if we only had one coin 
	if len(coins) == 1:
	# we'd only have to check if the amount % coin == 0 
	if coins[0] % amount == 0:
	return 1
​
	# if we have no coins and amount > 0
	if len(coins) == 0 and amount > 0:
	# there's no way to satisfy this; return 0 
	return 0
​
	# if amount == any of the coin denominations 
	# then that's one combination right there 
	# subtract the coin from the amount 
​
	# if we don't currently fall within any of these bases cases, how do we get to one of them? 
	# amount = 5, coins = [1, 2, 5]
​
	# take the latest coin and subtract it from amount 
​
	# we only ever took the last coin into account 
	return change(amount - coins[-1], coins) + change(amount, coins[:-1])