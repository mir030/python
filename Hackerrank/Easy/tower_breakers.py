# n = no. of towers
# m = the height of each tower
def tower_breakers(n, m):
    if n % 2 == 0 or m == 1:
        return 2
    else:
        return 1

