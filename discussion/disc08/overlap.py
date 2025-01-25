from link import *

def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)   # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    """
    # Recursion version
    if s is Link.empty or t is Link.empty:
        return 0
    
    if s.first == t.first:
        return 1 + overlap(s.rest, t.rest)
    elif s.first < t.first:
        return overlap(s.rest, t)
    else:
        return overlap(s, t.rest)
    """
    # Iteration version
    count = 0
    while s is not Link.empty and t is not Link.empty:
        if s.first == t.first:
            count, s, t = count + 1, s.rest, t.rest
        elif s.first < t.first:
            s = s.rest
        else:
            t = t.rest
    return count
