from link import *

def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.
    
    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    s = Link(0)
    s.first, s.rest = s, s
    return s
