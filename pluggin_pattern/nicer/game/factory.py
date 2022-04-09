from typing import Any, Callable
from game.character import GameCharacter


charactor_creation_funcs: dict[str, Callable[..., GameCharacter]] = {}


def register(character_type: str, creation_func: Callable[..., GameCharacter]):
    """register a new char type"""
    charactor_creation_funcs[character_type] = creation_func


def unregister(character_type: str):
    charactor_creation_funcs.pop(character_type, None)


def create(arguments: dict[str, Any]) -> GameCharacter:
    """Create a game char"""

    args_copy = arguments.copy()
    char_type = args_copy.pop("type")
    try:
        creation_func = charactor_creation_funcs[char_type]
        return creation_func(**args_copy)
    except KeyError:
        raise ValueError(f"unknown char: {char_type}")
