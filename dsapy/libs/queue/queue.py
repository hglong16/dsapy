from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

from dsapy.libs.linked_list.doubly_linked_list import DoublyLinkedList


class Queue[T](ABC):
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def enqueue(self, value: T) -> bool:
        raise NotImplementedError

    @abstractmethod
    def dequeue(self) -> T | None:
        raise NotImplementedError

    @property
    @abstractmethod
    def peek(self) -> T | None:
        raise NotImplementedError


@dataclass
class QueueList[T](Queue[T]):
    _list: List[T] = field(default_factory=list)

    @property
    def is_empty(self) -> bool:
        print(len(self._list))
        return len(self._list) == 0

    def enqueue(self, value: T) -> bool:
        self._list.append(value)
        return True

    def dequeue(self) -> T | None:
        return None if self.is_empty else self._list.pop(0)

    def peek(self) -> T | None:
        return None if self.is_empty else self._list[0]

    def __str__(self) -> str:
        return f"[{', '.join([str(value) for value in self._list])}]"


class QueueLinkedList[T](Queue[T]):
    _list = DoublyLinkedList[T]()

    @property
    def is_empty(self) -> bool:
        return self._list.is_empty

    def enqueue(self, value: T) -> bool:
        self._list.append(value)
        return True

    def dequeue(self) -> T | None:
        return self._list.pop()

    def peek(self) -> T | None:
        if self._list.head is None:
            return None
        return self._list.head.value

    def __str__(self) -> str:
        return str(self._list)
