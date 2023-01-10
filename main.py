# Functional Solution
def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

# Reflection
# 1)How does this solution ensure data immutability?
# By assigning the array's initial value within the method(function), we ensure immutability. Python will store this new object in a unique object’s address in memory.

# 2)Is this solution a pure function? Why or why not?
# It's a pure function. As you provide the same input, the function will always return the same output. This funciton will not produce side effects.

# 3)Is this solution a higher order function? Why or why not?
# No, it is not a higher order function because it does not accept one or more functions as an argument, nor does it return a function.

# 4)Would it have been easier to solve this problem using a different programming style?
# No

# 5)Why in particular is functional programming a helpful paradigm when solving this problem?
# It is a declarative type of programming style. Its main focus is on “what to solve” in contrast to an imperative style where the main focus is “how to solve”.

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        self.max_speed = self.max_speed * 2

class SubulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self,other):
        other.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism
# Answer:

# The classes "AnakinsPod" and "SebulbasPod" inherit from their parent class "Podracer" by setting their paramter to "Podracer".
# Using the super() method, "Podracer"'s attributes and methods are inherited when we create an instance of the "AnakinsPod" or "SebulbasPod" classes.
# We use Encapsulaion when constructing classes that have both attributes and methods.
# The flame_jet() function demonstrates Abstraction.
# We cannot instantiate an abstract class of "Podracer", but its abstract methods can be implemented by the subclass "SebulbasPod", as shown.

# --------------------------------------------------------------------------------------------------------------------
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# No, object oriented programming makes code more reusable, and makes it easier to work within larger programs.
# --------------------------------------------------------------------------------------------------------------------

# How in particular did Object Oriented Programming assist in the solving of this problem?
# OOP programs help you prevent repetition, as a class can be defined once and then reused many times.

# Reflection
# 1) Is one of these coding paradigms "better" than the other? Why or why not?
# No, depends on what we're trying to accomplish.

# 2) Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
# I find OOP more appealing as it mirrors the real world conceptually.

# 3) Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using:
# Functional Programming?
# Functional Programming would be good for Utilities and Service Oriented Solutions for simple data manipulation.
# Object Oriented Programming?
# OOP is good for almost all coding solutions

# 4) Personally, which of these styles takes more work to understand?
# Functional Programming but that is because I am used to OOP

# 5) What should be done in order to deepen understanding related to this paradigm?
# I need to study Functional Programming more as I think it would be useful for File and Data Utilities.