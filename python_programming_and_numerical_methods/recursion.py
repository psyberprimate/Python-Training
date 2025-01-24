

def chebuchev_poly_T_n(n : int, x : list):
    """Returns chebuchev polynomial of first type from list x
    """
    if n <= 0:
        y = [1] * len(x)
    elif n == 1:
        y = x
    else:
        y = [2 * x_iter * t_n_1 - t_n_2 for x_iter, t_n_1, t_n_2,
             in zip(x, chebuchev_poly_T_n(n=n-1, x=x), chebuchev_poly_T_n(n=n-2, x=x))]
    return y
    
    
def ackermann(m, n):
    """"Returns ackermann function solution for m and n
    """
    if m == 0:
        out = n + 1
    elif m > 0 and n == 0:
        out = ackermann(m=m-1, n=1)
    elif m > 0 and n > 0:
        out = ackermann(m=m-1, n=ackermann(m, n-1))
    return out

def unique_combinations_C(n, k):
    """Returns the unique ways of choosing k objects from n without repetion
    """
    if k < 1:
        raise Exception("k must be 1 or more")
    if k > n:
        raise Exception("k must be equal or less than n")
    if n==k:
        out = 1
    elif k==1:
        out = n
    else:
        out = unique_combinations_C(n=n-1, k=k) + unique_combinations_C(n=n-1, k=k-1)
    return out



x = [1, 2, 3, 4, 5]
print(f"\n\nchebuchev_poly_T_n(n, x): {chebuchev_poly_T_n(n=3, x=x)}")
print(f"\n\nackermann(m, n): {ackermann(m=3, n=4)}")
print(f"\n\nunique_combinations_C(n, k): {unique_combinations_C(n=10, k=4)}")