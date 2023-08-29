from create_one_attribute import Person

#create an object named "p1" whose name is "Anvar"
#create an object named "p2" whose name is "Shavkat"

class Person:
    def __init__(self,name,nam) -> None:
        self.name = name
        self.nam = nam

P1 = Person("Anvar")
P2 = Person("Shavkat")

print(P1.name)
print(P2.nam)