def comb(n,k):
    if n == k or k == 0:
        return 1
    elif k == 1:
        return n
    elif k <=n:
        return comb(n-1, k-1) + comb(n-1,k)
print(comb(5,2))