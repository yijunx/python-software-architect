from typing import Protocol


class GameCharacter(Protocol):
    """just a representation of a char"""

    def base_attack_motion(self) -> None:
        """the different base attacks of
        each char shall be implemented here
        """
