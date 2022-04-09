from dataclasses import dataclass
from game import factory


@dataclass
class Barb:
    name: str
    weapon: str = "axe"


    def base_attack_motion(self):
        print(f"swing my {self.weapon}!!!")

    def shout(self):
        """only barb can shout"""
        print("ya!!, ow!!, wa!!") 

def initialize() -> None:
    factory.register("barb", Barb)