from operator import floordiv, mod

def divide_exact(n, d):
    """Returns the quotient and remainder of dividing n by d
    >>> q, r = divide_exact(2026, 10)
    >>> q
    202
    >>> r
    5
    """
    return floordiv(n, d), mod(n, d)