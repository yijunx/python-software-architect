"""
basic example showing how to create objects from data using 
a dynamic factory with register/unregister methods
"""


import json
from dataclasses import dataclass
from game import factory, loader


@dataclass
class Sorcerer:
    name: str

    def base_attack_motion(self) -> None:
        print("fire ball!")


@dataclass
class Wizard:
    name: str

    def base_attack_motion(self) -> None:
        print("abracadabra!")


@dataclass
class Witcher:
    name: str

    def base_attack_motion(self) -> None:
        print("VOOOODOOOO!")


def main() -> None:
    """create game chars from a file"""

    # register the classes
    # what if we add a loader module, we can load class dynamically!!!
    factory.register("sorcerer", Sorcerer)
    factory.register("wizard", Wizard)
    factory.register("witcher", Witcher)

    # the below code will not need to change if we add new charactors
    with open("./level.json") as file:
        data = json.load(file)

        # load plugins before creation of charactor
        # so plugin can add new chars..
        # so now we dont need to change existing file anymore!!!!
        loader.load_plugins(data["plugins"])

        # create the chars
        chars = [factory.create(item) for item in data["characters"]]

        # do something with the chars
        for char in chars:
            print(char, end="\t")
            char.base_attack_motion()


if __name__ == "__main__":
    main()
