from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value, next) -> None:
        self.value: T = value
        self.next: Node[T] | None = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value}"
        return f"{self.value} -> {str(self.next)}"
