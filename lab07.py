# Car

class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)



# Keyboard

class Keyboard:
    """A Keyboard takes in a list of buttons, and has a
    dictionary of positions as keys, and Buttons as values.

    >>> b1 = Button("button1", "H")
    >>> b2 = Button("button2", "I")
    >>> k = Keyboard([b1, b2])
    >>> "button1" in k.buttons.keys() # Make sure to add the button to dictionary
    True
    >>> k.buttons["button1"].letter
    'H'
    >>> k.buttons["button1"].name
    'button1'
    >>> k.press("button1")
    'H'
    >>> k.press("button100")
    ''
    >>> b1.pressed
    1
    >>> b2.pressed
    0
    >>> k.typing(["button1", "button2"])
    'HI'
    >>> k.typing(["button2", "button1"])
    'IH'
    >>> b1.pressed # make sure typing calls press!
    3
    >>> b2.pressed
    2
    """

    def __init__(self, buttons):
        self.buttons = {}
        for button in buttons:
            self.buttons[button.name]=button

    def press(self, name):
        """Takes in a name of the button pressed, and
        returns that button's letter. Return an empty string 
        if the button does not exist. You can access the keys 
        of a dictionary d with d.keys(). """
        if name in self.buttons.keys():
            self.buttons[name].pressed = self.buttons[name].pressed+1
            return self.buttons[name].letter
        else:
            return ""

        

    def typing(self, typing_input):
        """Takes in a list of names of buttons to be pressed, and
        returns the total output. Make sure to call self.press"""
        result = ""
        for name in typing_input:
            result = result+self.press(name)
        return result
class Button:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
        self.pressed = 0

