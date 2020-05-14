def maximumToys(prices, k):
    count = 0
    total = 0
    prices.sort()
    for i in prices:
        total += i
        if total <= k:
            count+=1
    return count