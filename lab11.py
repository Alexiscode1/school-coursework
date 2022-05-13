#############
# Iterators #
#############

# Q1
class IteratorA:
    def __init__(self):
        self.start = 10

    def __next__(self):
        if self.start > 100:
            raise StopIteration
        self.start += 20
        return self.start

    def __iter__(self):
        return self

class IteratorB:
    def __init__(self):
        self.start = 5

    def __iter__(self):
        return self

class IteratorC:
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 10:
            raise StopIteration
        self.start += 1
        return self.start

class IteratorD:
    def __init__(self):
        self.start = 1

    def __next__(self):
        self.start += 1
        return self.start

    def __iter__(self):
        return self


# Q2
class Str:
    def __init__(self,string):
        self.string=string
        self.index=0

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        letter=self.string[self.index]
        self.index= self.index+1
        return letter

    def __iter__(self):
        return self


##############
# Generators #
##############

# Q3 
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    while n>=0:
        yield n
        n=n-1

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    
    def __init__(self,num):
        self.start =num

    def __iter__(self):
        while self.start >=0:
            yield self.start
            self.start=self.start-1



def naturals(initial=1, step=1):
    i = initial
    while True:
        yield i
        i += step

# Q4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for elem in s:
        yield elem*k


# Q5 
def pairs(lst):
    """
    >>> type(pairs([3, 4, 5]))
    <class 'generator'>
    >>> for x, y in pairs([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    for i in lst:
        for h in lst:
            yield(i,h)


