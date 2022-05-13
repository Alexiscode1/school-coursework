# Question 1
def odd_even(x):
    """Classify a number as odd or even.
    
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    if x%2 ==0:
        return "even"
    else:
        return "odd"

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    
    return list(map(odd_even, s))
   


# Question 2
def if_this_not_that(i_list, this):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for i in i_list:
        if i > this:
            print (i)
        else:
            print("that")


# Question 3
def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

     >>> shuffle(range(6))
     [0, 3, 1, 4, 2, 5]
     >>> suits = ['H', 'D', 'S', 'C']
     >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
     >>> cards[:12]
     ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
     >>> cards[26:30]
     ['7S', '7C', '8H', '8D']
     >>> shuffle(cards)[:12]
     ['AH', '7S', 'AD', '7C', 'AS', '8H', 'AC', '8D', '2H', '8S', '2D', '8C']
     >>> shuffle(shuffle(cards))[:12]
     ['AH', '4D', '7S', '10C', 'AD', '4S', '7C', 'JH', 'AS', '4C', '8H', 'JD']
     >>> cards[:12] # Should not be changed
     ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
     """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    num = int(len(cards)/2)
    lst1 = cards[:num]
    lst2 = cards[num:]
    strg = []
    for i in range(num):
        strg.append(lst1[i])
        strg.append(lst2[i])
    return list(strg)


# Question 4

def pairs(n):
    """Returns a new list containing two element lists from values 1 to n
    >>> pairs(1)
    [[1, 1]]
    >>> x = pairs(2)
    >>> x
    [[1, 1], [2, 2]]
    >>> pairs(5)
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    >>> pairs(-1)
    []
    """
    if n < 1:
        return []
    else:
        return [ [i,i] for i in range(1,n+1)]
    


# Question 5
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> def fn(x):
    ...     return x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[i, fn(i)] for i in seq if lower<=fn(i) & fn(i) <=upper ]
    


