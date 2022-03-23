from typing_extensions import Protocol


class Transaction(Protocol):
    def execute(self) -> None:
        ...

    def undo(self) -> None:
        ...

    def redo(self) -> None:
        ...
