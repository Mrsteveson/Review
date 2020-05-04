def sockMerchant(n, ar):
    c = Counter()
    for i in ar:
        c[i] = c.get(i,0) + 1

    return (sum([c[i]//2 for i in c]))