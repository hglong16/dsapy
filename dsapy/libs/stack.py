from typing import TypeVar, Generic, List, Optional

E = TypeVar("E")


class Stack(Generic[E]):
    def __init__(self) -> None:
        self._storage: List[E] = []

    def push(self, value: E) -> None:
        self._storage.append(value)

    def pop(self) -> Optional[E]:
        if self.isNotEmpty:
            return self._storage.pop()
        else:
            return None

    def peek(self) -> Optional[E]:
        if self.isNotEmpty:
            return self._storage[-1]
        else:
            return None

    @property
    def isEmpty(self) -> bool:
        return len(self._storage) == 0

    @property
    def isNotEmpty(self) -> bool:
        return len(self._storage) > 0

    def __str__(self) -> str:
        return f"""
            --- Top ---\n
            {self._storage}\n
            --- Bottom ---
            """
