class MyClass:
    a = 3
    b = "hi"

m = MyClass()

print(m.a, m.b)

n = MyClass()
n.a = 4

print(f"{n.a=}", f"{m.a=}")
# n.a=4 m.a=3
# we see that n.a has been updated
# but m is not affected

MyClass.a = 10 # normally we dont do this..

print(f"{n.a=}", f"{m.a=}")
# n.a=4 m.a=10
# we see that, m.a is changed due to MyClass.a changed
# but n stay unchanged!!

class MyNewClass(MyClass):
    k = 9
new_m = MyNewClass()

print(f"{new_m.a=},{new_m.k=}")
# new_m.a=10,new_m.k=9


class ClassUsingInstanceVariables:
    def __init__(self, a) -> None:
        self.a = a
        pass


proper_m = ClassUsingInstanceVariables(a=3)
print(f"{proper_m.a=}")
# proper_m.a=3


# use them both
class Shark:

    # Class variables
    # so you dont have to put them in init
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def bite(self, what):
        print(f"{self.name} (a {self.animal_type}, age {self.age}) bites {what} at {self.location}")


s = Shark(name="tom", age=10)
s.bite(what="sea weed")
# tom (a fish, age 10) bites sea weed at ocean