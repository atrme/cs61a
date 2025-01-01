def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        """ The recursive case is to choose the larger of "the 1st element times max_product of 
        the rest elements starting from index 2" and "the 2nd element times max_product of the 
        rest elements starting from index 3" """
        return max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))
