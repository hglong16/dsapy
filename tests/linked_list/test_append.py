from dsapy.libs.linked_list import LinkedList


class TestLinkedList:
    def test_append(self):
        linked_list = LinkedList[int]()
        linked_list.append(5)
        linked_list.append(6)
        linked_list.append(7)
        assert str(linked_list) == "5 -> 6 -> 7"
        assert str(linked_list) == "5 -> 6 -> 7"

    def test_insert_after(self):
        linked_list = LinkedList[int]()
        linked_list.append(5)
        linked_list.append(6)
        linked_list.append(8)

        node_6 = linked_list.node_at(1)
        assert node_6 is not None and node_6.value == 6

        linked_list.insert_after(node_6, 7)
        assert str(linked_list) == "5 -> 6 -> 7 -> 8"

    def test_insert_after_2(self):
        linked_list = LinkedList[int]()

        linked_list.push(8)
        linked_list.push(6)
        linked_list.push(5)

        node_6 = linked_list.node_at(1)
        assert node_6 is not None and node_6.value == 6

        linked_list.insert_after(node_6, 7)
        assert str(linked_list) == "5 -> 6 -> 7 -> 8"

    def test_pop(self):
        linked_list = LinkedList[int]()
        linked_list.append(5)
        linked_list.append(6)
        linked_list.append(7)
        assert linked_list.pop() == 5
        assert str(linked_list) == "6 -> 7"

    def test_remove_last(self):
        linked_list = LinkedList[int]()

        linked_list.append(5)
        linked_list.append(6)
        linked_list.append(7)

        node_remove = linked_list.remove_last()

        assert node_remove is not None and node_remove == 7

        assert str(linked_list) == "5 -> 6"
