# 00P

class Person(object):
    """
    >>> steven = Person("Steven")
    >>> barb = Person("Barb")
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> barb.ask("listen to me repeat myself")
    'Would you please listen to me repeat myself'
    >>> barb.repeat()
    'Would you please listen to me repeat myself'
    >>> steven.repeat()
    'Hello, my name is Steven'
    """
    def __init__(self, name):
        self.name = name
        self.sentence=[]

    def say(self, stuff):
        self.sentence.append(stuff)
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        return self.sentence[-1]


class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> sophia_account = Account('Sophia')
    >>> sophia_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> sophia_account.transactions
    [('deposit', 1000000)]
    >>> sophia_account.withdraw(100)      # buying dinner
    999900
    >>> sophia_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02
    balance = 1000

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('withdraw', amount))
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Out of stock'
    >>> v.restock(2)
    'Stock: 2'
    >>> v.vend()
    'Please deposit $10 more'
    >>> v.deposit(7)
    'Current Balance: $7'
    >>> v.vend()
    'Please deposit $3 more'
    >>> v.deposit(5)
    'Current Balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change'
    >>> v.deposit(10)
    'Current Balance: $10'
    >>> v.vend()
    'Here is your candy'
    >>> v.deposit(15)
    'Out of stock. Here is your $15'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock==0:
            return 'Out of stock'
        if self.balance<self.price:
            needed=self.price-self.balance
            return "Please deposit ${} more".format(needed)
        if self.balance==self.price:
            self.stock= self.stock-1
            return 'Here is your '+ self.product
        
        else:
            change = self.balance-self.price
            self.balance=0
            self.stock =self.stock-1
            return 'Here is your '+ self.product+' and ${} change'.format(change)
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        if self.stock>0:
            return 'Current Balance: ${}'.format(self.balance)
        else:
            return 'Out of stock. Here is your ${}'.format(amount)
        
    
    def restock(self, number):
        self.stock = self.stock+number
        return 'Stock: {}'.format(self.stock)


class Arr88():
    """
    Arr88 is an object similar to Data 8 numpy arrays.
    Here the internel representation is a list
    """
    def __init__(self, values):
        # Check that all values are the same type, else it errors
        if len(values) > 1:
            assert all([type(values[0]) == type(values[i]) for i in range(len(values))]), "Arr88 must be of homogeneous type"
        self._values = values

    # DO NOT CHANGE THE __repr__
    # This displays the Arr88 nicely in the terminal
    def __repr__(self):
        return "Arr88(" + str(self._values) + ')'

    def __len__(self):
        """ Return the length of the Arr88

        >>> arr88 = Arr88([1, 2, 3])
        >>> len(arr88)
        3
        >>> arr88 = Arr88([1, 2, 3, 4])
        >>> len(arr88)
        4
        """
        return len(self._values)
        

    def item(self, i):
        """
        Get the item of the Arr88 at index i
        >>> arr88 = Arr88([1, 2, 3])
        >>> arr88.item(1)
        2
        >>> arr88.item(0)
        1
        """
        return self._values[i]
        

    def __add__(self, arr88):
        """ Add two Arr88s of the same length element by element

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4, 5, 6])
        >>> arr88a + arr88b
        Arr88([5, 7, 9])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88a = Arr88(['He', 'Wor', '!'])
        >>> arr88b = Arr88(['llo', 'ld', ''])
        >>> arr88c = arr88a + arr88b
        >>> arr88c
        Arr88(['Hello', 'World', '!'])
        """
        # Checks that the lengths are the same
        assert len(self) == len(arr88), "Arr88's of different len"
        return Arr88([self._values[i]+arr88._values[i] for i in range(len(self))])
        

    def __mul__(self, arr88):
        """ Multiply two Arr88s of the same length componentwise

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4, 5, 6])
        >>> arr88a * arr88b
        Arr88([4, 10, 18])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88a = Arr88(['Na', 'Batman', '!'])
        >>> arr88b = Arr88([10, 1, 5])
        >>> arr88c = arr88a * arr88b
        >>> arr88c
        Arr88(['NaNaNaNaNaNaNaNaNaNa', 'Batman', '!!!!!'])
        """
        # Checks that the lengths are the same
        assert len(self) == len(arr88), "Arr88's of different len"
        return Arr88([self._values[i]*arr88._values[i] for i in range(len(self))])
        

    def negate(self):
        """Negate an Arr88 with mutation

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4.0, -5.5, 0.0])
        >>> arr88a.negate()
        >>> arr88a
        Arr88([-1, -2, -3])
        >>> arr88b.negate()
        >>> arr88b
        Arr88([-4.0, 5.5, -0.0])
        """
        self._values = [-value for value in self._values]
        


    def apply(self, func):
        """ Apply a function to an Arr88

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88a.apply(lambda x : x * x)
        Arr88([1, 4, 9])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88b = Arr88([lambda x: x, lambda x: x + 1, lambda x: x + 2])
        >>> arr88c = arr88b.apply(lambda f: f(1))
        >>> arr88c
        Arr88([1, 2, 3])
        """
        return Arr88(list(map(func, self._values)))
        




