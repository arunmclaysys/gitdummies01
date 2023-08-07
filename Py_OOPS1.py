#OOPS Concepts

#Constructor
class Soldier:
    def __init__(self, armor, num_weapons):  #these are instace variables
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier(5, 10)
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"