def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    prev, succ = next(t), None
    for elem in t:
        succ = elem 
        yield succ - prev
        prev = succ
