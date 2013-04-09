def combinations(n,r):
    if r == 0:
        return 1
    else:
        if r == n:
            return 1
        else:
            return combinations(n-1,r-1) + combinations(n-1,r)        
