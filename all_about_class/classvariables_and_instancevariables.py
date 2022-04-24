class SomeClass:

    class_variable = "class_variable_value"

    def __init__(self, instance_variable_value) -> None:
        self.instance_variable = instance_variable_value


if __name__ == "__main__":

    x = SomeClass("x")
    y = SomeClass("y")

    print(x.class_variable)
    print(y.instance_variable)
    print(SomeClass.class_variable)
    # print(SomeClass.instance_variable) will not work

    # now lets change something
    SomeClass.class_variable = "updated!"
    print(y.class_variable) # well its updated

    # now lets update in another way
    y.class_variable = "updated for y"
    print(y.class_variable)
    print(x.class_variable)  # not updated
    print(SomeClass.class_variable)  # not updated


