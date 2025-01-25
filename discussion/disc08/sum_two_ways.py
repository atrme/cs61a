from link import *

def sum_rec(s, k):
    """Return the sum of thr first k elements in s.
    
    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_rec(a, 2)
    7
    >>> sum_rec(a, 5)
    15
    >>> sum_rec(Link.empty, 1)
    0
    """
    # Use a recursive call to sum_rec; don't call sum_iter
    if s is Link.empty or k == 0:
        return 0
    else: 
        return s.first + sum_rec(s.rest, k-1)

def sum_iter(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_iter(a, 2)
    7
    >>> sum_iter(a, 5)
    15
    >>> sum_iter(Link.empty, 1)
    0
    """
    # Don't call sum_rec or sum_iter
    result = 0
    while s is not Link.empty and k != 0:
        result += s.first   # Accumulate summation
        # Loop processing
        s = s.rest
        k -= 1
    return result
