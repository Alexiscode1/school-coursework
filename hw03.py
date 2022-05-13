######################
# Required Questions #
######################

def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    >>> matrix4 = [[ 1, -2,  3],
    ...            [-4,  5, -6]]
    >>> matrix5 = [[-1,  2, -3],
    ...            [ 4, -5,  6]]
    >>> add_matrices(matrix4, matrix5)
    [[0, 0, 0], [0, 0, 0]]
    """
    return [[x[0][i]+y[0][i] for i in range(len(x[1]))],[x[1][i]+y[1][i] for i in range(len(x[1]))]]
    


def mul_by_num(factor):
    """
    Returns a function that takes one argument and
    returns the product of factor and that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    def inner(argument):
        return argument*factor
    return inner
    


def make_derivative(f):
    """Returns a function that approximates the derivative of f.

    Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
    approximate the derivative by choosing a very small value for h.

    >>> def square(x): 
    ...     # equivalent to: square = lambda x: x*x
    ...     return x*x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3) # approximately 2*3
    6.0
    """
    h=0.00001
    def derivative(a):
        return (f(a+h)-f(a))/h
    return derivative


def count_cond(mystery_function, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    count =0
    i=1
    while i<=n:
        if mystery_function(n,i):
            count = count+1
            i = i+1
        else:
            i = i+1
    return count
    


def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    
    def my_cycle(n):
        def inner(x):
            if int(n/3)>0:
                i=0
                while i < int(n/3):
                    x= f3(f2(f1(x)))
                    i =i+1
                if n%3 == 0:
                    return x
                elif n%3 ==1:
                    return f1(x)
                elif n%3 ==2:
                    return f2(f1(x))
                else:
                    return f3(f2(f1(x))) 
            else:
                if  n==0:
                    return x
                elif n ==1:
                    return f1(x)
                elif n ==2:
                    return f2(f1(x))
                else:
                    return f3(f2(f1(x)))
        return inner            
    return my_cycle


def store_word(secret):
    """
    >>> word_len, guess_word = store_word("cake")
    >>> word_len
    4
    >>> guess_word("corn")
    [True, False, False, False]
    >>> guess_word("come")
    [True, False, False, True]
    >>> guess_word("cake")
    [True, True, True, True]
    >>> word_len, guess_word = store_word("pop")
    >>> word_len
    3
    >>> guess_word("ate")
    [False, False, False]
    >>> guess_word("top")
    [False, True, True]
    >>> guess_word("pop")
    [True, True, True]
    """
    word_len = len(secret)
    lst1 = [i for i in secret]
    
    
    def guess_word(var):
        result = []
        lst2 = [i for i in var]
        for i in range(word_len):
            if lst1[i]==lst2[i]:
                result.append(True)
            else:
                result.append(False)
        return result
        
    return word_len, guess_word

