
###################################
## Iterator/Generator Questions ##
###################################

def naturals(initial=1, step=1):
    i = initial
    while True:
        yield i
        i += step

# Q1
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start=start-1
        self.restart=self.start
        self.end=end

    def __next__(self):
        if self.start!=self.end:
            self.start= self.start+1
            return self.start
        else:
            self.start=self.restart
            raise StopIteration
    
    def __iter__(self):
        return self


# Q2
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    num=n
    while num>=1:
        if num==1:
            yield int(num)
            return
        if num%2==0:
            yield int(num)
            num=num/2
        else:
            yield int(num)
            num=num*3+1



# Q3
def generate_perms(lst):
    """
    Generates the permutations of lst one by one.
    >>> perms = generate_perms([1, 2, 3])
    >>> hasattr(perms, '__next__')
    True
    >>> p = list(perms)
    >>> p.sort()
    >>> p
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if lst==[]:
        yield []
        return
    elif len(lst)==1:
        yield lst
        return
    else:
        for elem in generate_perms(lst[1:]):
            for h in range(len(lst)):
                yield elem[:h] + [lst[0]] + elem[h:] #to insert lst[0] value into different positions


