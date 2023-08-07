#Inheritance

#In order to use the constructor of the parent class, we can use Python's built in super() method.

class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

    def has_tail(self):
        return True

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to give the cow some legs
        super().__init__(4)
        #Animal.__init__(4) #This throws an error
        #Animal.__init__(self,4) #This Works
        #Animal.has_tail(self) #This works
        self.wings = True
        
info = Animal(2)
print(info.num_legs)
print(info.has_tail())
specific_info = Cow()
print(specific_info.num_legs)
print(specific_info.wings)