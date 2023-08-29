from create_one_attribute import Person

#create an object named "person" whose name is "Ali"
class Person:
    def __init__(self,name) -> None:
        self.name=name
person = Person("Ali")

print(person.name)