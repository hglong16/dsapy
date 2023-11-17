from dsapy.libs.linked_list import LinkedList


def test_remove_all():
    linked_list = LinkedList()

    linked_list.push(3)
    linked_list.push(5)
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(3)
    linked_list.push(1)

    linked_list.remove_all(3)
    assert str(linked_list) == "1 -> 4 -> 5"
