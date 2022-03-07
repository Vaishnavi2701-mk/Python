def recursivesum(n):
    if n==1:
        return 1
    else:
        return n+recursivesum(n-1)

s=recursivesum(20)
print(s)               