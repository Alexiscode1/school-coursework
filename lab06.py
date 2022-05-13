def sum(n):
    """Using recursion, computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    if n==1:
        return 1
    else:
        return n+sum(n-1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k==7:
        return True
    elif k//10 ==0:
        return False
    else:
        return has_seven(k//10) or has_seven(k%10)


def filter(f, seq):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    if len(seq)==1:
        if f(seq[0]):
            return seq
        else:
            return None
        
    else:
        x=filter(f, seq[:len(seq)-1])
        if x is None:
            x =[]
            return x+[seq[i] for i in range((len(seq)-1),len(seq)) if f(seq[len(seq)-1])]
        else:
            return x+[seq[i] for i in range((len(seq)-1),len(seq)) if f(seq[len(seq)-1])]


def decimal(n):
    """Return a list representing the decimal representation of a number.

    >>> decimal(55055)
    [5, 5, 0, 5, 5]
    >>> decimal(-136)
    ['-', 1, 3, 6]
    """
    if n <0:
        n =-n
        lst =["-"]
        return lst+(decimal(n))
        
    elif n//10==0:
        return [n]
    else:
        return decimal(n//10)+[n%10]
        



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
    if m==1 or n==1:
        return 1
    else:
        return paths(m-1,n) + paths(m,n-1)

