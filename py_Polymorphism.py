#Polymorphism

#methods with the same name but different behaviors.

#In this example the child classes, Hydra and Kraken are overriding the behavior of their parent class's move() method.

class Creatures:
    def moves(self):
        print("Creature moves")

class Kraken(Creatures):
    def moves(self):
        print("Krakken moves")

class Hydra(Creatures):
    def moves(self):
        print("Hydra moves")

for creature in [Creatures(), Kraken(), Hydra()]:
    creature.moves()


###############--------another example - different function signatures------#######
class Human:
    def __init__(self, health):
        self.health = health
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer(Human):
    def hit_by_fire(self, dmg):
        self.health -= dmg
        return self.health
        
h = Human(15)
print(h.hit_by_fire())

a = Archer(50)
print(a.hit_by_fire(25))

##########---Method Overloading Example----------##############
#The __add__ method is used by the Python interpreter when instances of a class are being added with the + operator.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)

    def __repr__(self):     #The __repr__ method (short for "represent")
        return f'({self.x},{self.y})'

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2  #When you call p1 + p2 under the hood the interpreter just calls p1.__add__(p2).
print(p3)
