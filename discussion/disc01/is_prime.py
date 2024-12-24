def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n == 1:
        return False # one is neither a prime number nor a multiple number
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
