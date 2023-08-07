#Abstraction

#Abstraction is a technique that helps us identify what information and behavior should be encapsulated, and what should be exposed.
#Encapsulation is the technique for organizing the code to encapsulate what should be hidden, and make visible what is intended to be visible.

#The process of using the double underscore is a form of encapsulation. The process of deciding which data deserves to be hidden behind the double underscore is abstraction.

# Creating a Base class
class Base:

	# Declaring public method
	def fun(self):
		print("Public method")

	# Declaring private method
	def __fun(self):
		print("Private method")

# Creating a derived class
class Derived(Base):
	def __init__(self):
		# Calling constructor of
		# Base class
		Base.__init__(self)

	def call_public(self):
		# Calling public method of base class
		print("\nInside derived class")
		self.fun()

	def call_private(self):
		# Calling private method of base class
		self.__fun()

# Driver code
obj1 = Base()

# Calling public method
obj1.fun()

obj2 = Derived()
obj2.call_public()
  
obj1.__fun() #Uncomment it as it raises an AttributeError

obj2.call_private() #Uncomment it as it raises an AttributeError

#The below code will work fine
obj1._Base__fun() #This method is known as name mangling. please dont use dot between _Base and __fun()