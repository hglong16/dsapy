from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Node[T] | None = None

    def __init__(self, value, next) -> None:
        self.value: T = value
        self.next: Node[T] | None = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value}"
        return f"{self.value} -> {str(self.next)}"


@dataclass
class LinkedList(Generic[T]):
    """Linked list implementation

    Args:
        Generic (_type_): _description_ (default: {_default_})

    Returns:
        _type_: _description_
    """

    head: Node[T] | None = None
    tail: Node[T] | None = None

    @property
    def is_empty(self) -> bool:
        return self.head is None

    def node_at(self, index: int) -> Node[T] | None:
        """Returns the node at the given index

        Args:
            index (int): The index of the node to be returned

        Returns:
            Node[T] | None: The node at the given index
        """

        current_node = self.head
        current_index = 0

        while current_node is not None and current_index < index:
            current_node = current_node.next
            current_index += 1

        return current_node

    def push(self, value: T) -> None:
        """Pushes a value to the head of the linked list

        Args:
            value (T): The value to be pushed
        """
        self.head = Node(value, self.head)
        if self.tail is None:
            self.tail = self.head

    def append(self, value: T) -> None:
        """Appends a value to the tail of the linked list

        Args:
            value (T): The value to be appended
        """

        if self.is_empty:
            self.push(value)
            return

        if self.tail is not None:
            self.tail.next = Node(value, None)
            self.tail = self.tail.next

    def insert_after(self, node: Node[T], value: T) -> Node[T]:
        """insert_after node

        Args:
            node (Node[T]): node in LinkedList
            value (T): value insert

        Returns:
            Node[T]: Node inserted
        """
        if self.tail == node:
            self.append(value)
            return self.tail  # type: ignore

        node.next = Node(value, node.next)
        return node.next

    def pop(self) -> T | None:
        """Pops the head of the linked list

        Returns:
            T | None: The value of the popped node
        """
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next

        if self.is_empty:
            self.tail = None

        return value

    def remove_last(self) -> T | None:
        """Remove last node

        Returns:
            T | None: Value of last node
        """

        if self.head is None or self.tail is None:
            return None

        if self.head.next is None:
            return self.pop()

        current_node = self.head
        while current_node.next is not None and current_node.next != self.tail:
            current_node = current_node.next

        value = self.tail.value

        self.tail = current_node
        current_node.next = None

        return value

    def remove_after(self, node: Node[T]) -> T | None:
        """Remove node after node

        Args:
            node (Node[T]): Node in LinkedList

        Returns:
            T | None: Value of node removed
        """
        if node.next is None:
            return None

        if node.next == self.tail:
            return self.remove_last()

        value = node.next.value
        node.next = node.next.next

        return value

    def __iter__(self) -> LinkedList[T]:
        return self

    def __next__(self) -> T:
        if self.is_empty:
            raise StopIteration
        return self.pop()  # type: ignore

    def __str__(self) -> str:
        if self.is_empty:
            return "Empty list"
        return str(self.head)
