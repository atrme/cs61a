def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def f(i):
        """Returns False if n % i == 0. Otherwise, it recursively calls itself on (i + 1) until
           i reaches n and returns True"""
        if i >= n:
            return True
        elif n % i == 0:
            return False
        else:
            return f(i + 1)

    if n == 1:
        return False
    return f(2)
