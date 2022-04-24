class SomeClass:

    class_variable = "class_variable_value"

    def __init__(self, instance_variable_value) -> None:
        self.instance_variable = instance_variable_value

    
    @staticmethod
    def this_is_a_static_method(anything):
        """well this is a staticmethod, takes nothing from
        cls or instance as first argument...
        
        so i am not sure why this is in a class..
        this reduces the code coherence."""
        return anything
    

    def this_is_an_instance_method(selfff):
        """the instance method takes the first argument as 'self'.
        so when use it, the self or the instance is auto provided
        and the first argument has to be the instance itself, thus self

        here i can name it selfff also ok. but the convention is self
        """
        print(f"hihi i am {selfff}")

    @classmethod
    def this_is_an_class_method(cls):
        """the class methos takes the first argument as its class,
        this requires a decorator. so when use it, the class is auto provided.
        and the first atgument has to be the class itself, thus cls
        """
        print(cls.class_variable)


    @classmethod
    def update_class_variable(cls, v):
        """the class methos takes the first argument as its class,
        this requires a decorator. so when use it, the class is auto provided.
        and the first atgument has to be the class itself, thus cls
        """
        cls.class_variable = v

    @classmethod
    def from_other_stuff(cls, otherstuff):
        """use from xxxx as convention to create another way to generate new instances"""
        return cls(f"otherstuff: {otherstuff}")
        


if __name__ == "__main__":

    x = SomeClass("x")
    print(x.this_is_an_instance_method())
    y = SomeClass("y")

    print(x.class_variable)
    print(y.instance_variable)
    print(SomeClass.class_variable)
    # print(SomeClass.instance_variable) will not work

    # now lets change something
    SomeClass.class_variable = "updated!"
    print(y.class_variable) # well its updated

    # now lets update in another way
    # now all updated..
    y.update_class_variable("updated for y but works for all with classmethod")
    print(y.class_variable)
    print(x.class_variable)
    print(SomeClass.class_variable)

    z = SomeClass.from_other_stuff("z")
    print(z.instance_variable)

    print(z.this_is_a_static_method("hihi"))
    


