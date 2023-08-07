#Inheritance

#In order to use the constructor of the parent class, we can use Python's built in super() method.

class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to give the cow some legs
        super().__init__(4)
        #Animal.__init__(4) #This throws an error
        self.wings = True
        
info = Animal(2)
print(info.num_legs)
specific_info = Cow()
print(specific_info.num_legs)
print(specific_info.wings)