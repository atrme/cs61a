from math import gcd
from link import *

def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')

def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)    # The zero before the decimal point

    def simplify_fraction(n, d):
        f = gcd(n, d)
        return n//f, d//f

    def find_k(n):
        """Find a number k such that (10 ** k - 1) can evenly be divided by n."""    
        # Number k will never be found if n has factor 2 or 5
        assert n % 2 != 0 and n % 5 != 0, 'Infinite loop!'
        k = 1
        while True: 
            if (10 ** k - 1) % n == 0:
                return k
            k += 1  

    def build_loop_link(n, k):
        """
        Given an integer n and k indicating k digits for a cycle.
        Build a linked list whose last node's rest is the first node.
        
        >>> a = 123
        >>> b = build_loop_link(a, 4)           #  _>0 -> 1 -> 2 -> 3_
        >>> b.rest.rest.rest.rest.first         # |___________________|
        0
        """
        digits = str(n)
        digits = ('0' * (k - len(digits))) + digits
        link = Link(int(digits[-1]))
        last = link
        for digit in reversed(digits[0:-1]):
            link = Link(int(digit), link)
        last.rest = link
        return link
    
    def remove_2_5(d):
        """Divide d by 2 or 5, until d has no factor 2 or 5.

        >>> remove_2_5(30)  # 2 * 5 * 3
        3
        """
        while d % 2 == 0:
            d = d // 2
        while d % 5 == 0:
            d = d // 5
        return d

    n, d = simplify_fraction(n, d)
    d_without_2_5 = remove_2_5(d)
    d, scale = d_without_2_5, d // d_without_2_5
    if scale > 1:   # d has factor 2 or 5
        """e.g.    1/6          # 6 has factor 2
                -> 1/2 * 1/3    # Now 3 has no factor 2 or 5 
                -> 1/10 * 5/3   # Take 1/10 out of 1/2, represented by l_shift = 1
                -> 1/10 * (1+2/3)   # Turn improper fraction into proper fraction
                # Now we can normally compute the loop part of 2/3, which is also the 
                  loop part of 1/6. (2/3: 0.666..., 1/6: 0.1666..., both has 666...)
                # Difference in fraction between 1/6 and 2/3 can be eliminated by 
                  shifting decimal point or adding number before the loop part 
        """
        # Find the smallest l_shift such that scale is a factor of (10 ** l_shift)
        l_shift = 1
        while (10 ** l_shift) % scale != 0:
            l_shift += 1
        n = n * (10 ** l_shift // scale)
        # Turn improper fraction into proper fraction
        carry = n // d
        n -= carry * d
        # The digits after decimal point and before the loop part
        before_loop = build_loop_link(carry, l_shift)

    else:  # d has no factor 2 or 5
        pass

    k = find_k(d)
    pattern = (10 ** k - 1) * n // d     # A pattern that will cycle in the decimal
    loop = build_loop_link(pattern, k)            # Build a loop link on certain pattern
    if scale > 1:
        # Concatnate `before_loop` and `loop`
        pointer = before_loop
        # Given `before_loop` is constructed by function `build_loop_link`, the pointer
        # points to the last node when pointer.rest is `before_loop`
        while pointer.rest is not before_loop: 
            pointer = pointer.rest
        pointer.rest = loop 
        result.rest = before_loop 
    else:
        result.rest = loop
    return result
