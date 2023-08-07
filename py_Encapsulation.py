#Encapsulation - Encapsulation is the practice of hiding information inside of a "black box" 
#so that other developers working with the code don't have to worry about it.
#This is the process of wrapping the data and object/code together in a single unit.
#This is done by restricting access to some of the data members and methods.
#This prevents the data from being accessed or modified from outside the class. 
  
class Wall():
    def __init__(self, height):
        # this stops us from accessing the __height
        # property directly on an instance of a Wall. Here __ refers to private varlable.
        self.__height = height

    def get_height(self):
        return self.__height
    
mywall = Wall(10)
print(mywall.get_height()) #output is 10

mywall.__height = 120
print(mywall.__height) #output is 120
print(mywall.get_height()) #output is 10- it is like instance variables

mywall._Wall__height = 130
print(mywall._Wall__height) #output is 130

print(mywall.get_height()) #output is 130