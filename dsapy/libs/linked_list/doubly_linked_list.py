from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import Iterable, Self


@dataclass
class Node[T]:
    value: T
    next: Node[T] | None = None
    previous: Node[T] | None = None

    def __str__(self) -> str:
        return str(self.value)


class LinkedList[T](ABC):
    head: Node[T] | None
    tail: Node[T] | None

    @abstractproperty
    def is_empty(self) -> bool:
        return self.head is None or self.tail is None

    @abstractmethod
    def append(self, value: T) -> None:
        pass

    @abstractmethod
    def push(self, value: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T | None:
        pass

    @abstractmethod
    def remove_last(self) -> T | None:
        pass


@dataclass
class DoublyLinkedList[T](LinkedList[T], Iterable[T]):
    head: Node[T] | None = None
    tail: Node[T] | None = None

    @property
    def is_empty(self) -> bool:
        return self.head is None or self.tail is None

    def push(self, value: T) -> None:
        node = Node(value, next=self.head)

        if self.head is None or self.tail is None:
            self.tail = node
        else:
            self.head.previous = node

            if self.head.next is None:
                self.tail = self.head

        self.head = node

    def append(self, value: T) -> None:
        node = Node(value, previous=self.tail)

        if self.head is None or self.tail is None:
            self.head = node
        else:
            self.tail.next = node

            if self.tail.previous is None:
                self.head = self.tail

        self.tail = node

    def pop(self) -> T | None:
        if self.head is None or self.tail is None:
            return None

        value = self.head.value

        if self.head.next is None:
            self.tail = None
            self.head = None
            return value

        self.head = self.head.next
        self.head.previous = None
        return value

    def remove_last(self) -> T | None:
        if self.head is None or self.tail is None:
            return None

        value = self.tail.value
        if self.tail.previous is None:
            return self.pop()

        self.tail = self.tail.previous
        self.tail.next = None
        return value

    def __str__(self) -> str:
        if self.head is None or self.tail is None:
            return "[]"

        current = self.head
        result = "["
        while current is not None:
            result += str(current.value) + ", "
            current = current.next

        return result[:-2] + "]"

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> T | None:
        if self.head is None or self.tail is None:
            raise StopIteration
        return self.pop()
