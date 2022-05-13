######################
# Required Questions #
######################

# Probably a die-re situation

from operator import add, mul

def reduce(reducer, seq, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    if len(seq)==0:
        return None
    elif len(seq)==1:
        return reducer(base,seq[0])
    else:
        return reducer(reduce(reducer, seq[:-1],base),seq[-1])
    


def remove_last(x, s):
    """Create a new list that is identical to s but with the last
    element from the list that is equal to x removed.

    >>> remove_last(1,[])
    []
    >>> remove_last(1,[1])
    []
    >>> remove_last(1,[1,1])
    [1]
    >>> remove_last(1,[2,1])
    [2]
    >>> remove_last(1,[3,1,2])
    [3, 2]
    >>> remove_last(1,[3,1,2,1])
    [3, 1, 2]
    >>> remove_last(5, [3, 5, 2, 5, 11])
    [3, 5, 2, 11]
    """
    if s==[]:
        return []
    elif len(s)==1:
        if x==s[-1]:
            return []
        else:
            return s
    elif x==s[-1]:
        return s[:-1]
    else:
        return remove_last(x, s[:-1])+[s[-1]]


def binary(n):
    """Return a list representing the representation of a number in base 2.

    >>> binary(55055)
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    >>> binary(-136)
    ['-', 1, 0, 0, 0, 1, 0, 0, 0]
    """
    if n<0:
        n = -n
        return ["-"]+binary(n)
    elif n ==0:
        return []
    elif n ==1:
        return [1]
    else:
        return binary(n//2)+[n%2]


def hailstone_iterative(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_iterative(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    i=1
    while n!=1:
        print(n)
        i = i+1
        if n%2==0:
            
            n = int(n/2)
            
        else:
            
            n = n*3+1
    print(n)
    return i       


def hailstone_recursive(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_recursive(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(int(n))
    if n==1:
        
        return n
    else:
        if n%2==0:
            
            return int(hailstone_recursive(n/2)+1)
        else:
            
            return int(hailstone_recursive(n*3+1)+1)
     

def count_change(amount, denominations):
    """Returns the number of ways to make change for amount.

    >>> denominations = [50, 25, 10, 5, 1]
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = [16, 8, 4, 2, 1]
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    if amount==0:
        return 1
    elif amount<0 or len(denominations)==0:
        return 0
    else:
        use_coin= count_change(amount-denominations[0], denominations)
        not_use_coin = count_change(amount, denominations[1:])
        return use_coin+ not_use_coin

