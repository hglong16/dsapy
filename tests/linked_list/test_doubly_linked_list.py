from dsapy.libs.linked_list.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList:
    def test_is_empty(self):
        dll = DoublyLinkedList[int]()
        assert dll.is_empty

    def test_push(self):
        dll = DoublyLinkedList[int]()
        dll.push(1)
        assert dll.head is not None and dll.head.value == 1
        assert dll.tail is not None and dll.tail.value == 1

        dll.push(2)
        assert dll.head.value == 2
        assert dll.tail.value == 1

        dll.push(3)
        assert dll.head.value == 3
        assert dll.tail.value == 1

        assert str(dll) == "[3, 2, 1]"

    def test_append(self):
        dll = DoublyLinkedList[int]()
        dll.append(1)
        assert dll.head is not None and dll.head.value == 1
        assert dll.tail is not None and dll.tail.value == 1

        dll.append(2)
        assert dll.head.value == 1
        assert dll.tail.value == 2

        dll.append(3)
        assert dll.head.value == 1
        assert dll.tail.value == 3

        assert str(dll) == "[1, 2, 3]"

    def test_pop(self):
        dll = DoublyLinkedList[int]()
        dll.push(1)
        dll.push(2)
        dll.push(3)

        assert dll.pop() == 3
        assert dll.pop() == 2
        assert dll.pop() == 1
        assert dll.pop() is None

    def test_remove_last(self):
        dll = DoublyLinkedList[int]()
        dll.push(1)
        dll.push(2)
        dll.push(3)

        assert dll.remove_last() == 1
        assert dll.remove_last() == 2
        assert dll.remove_last() == 3
        assert dll.remove_last() is None

    def test_iter(self):
        dll = DoublyLinkedList[int]()
        dll.push(1)
        dll.push(2)
        dll.push(3)

        assert [i for i in dll] == [3, 2, 1]
