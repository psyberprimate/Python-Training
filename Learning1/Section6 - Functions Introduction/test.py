def sum_eo(n, t):
    value = 0
    if t == "e":
        for i in range(1,n):
             if (i % 2) == 0:
                 value += i
    elif t == "o":
        for i in range(1,n):
             if (i % 2) != 0:
                 value += i
    else:
        return -1
    return value   

print(sum_eo(10, "o"))

