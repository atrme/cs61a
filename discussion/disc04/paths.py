def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:    # A m*1 grid means only 1 available path
        return 1
    
    # To reach a cell, it must first get to the cell on its left or below it
    return paths(m-1, n) + paths(m, n-1)
