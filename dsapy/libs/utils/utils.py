from dsapy.libs.linked_list import LinkedList


def create_linked_list() -> LinkedList[int]:
    """Return sample linked list

    Returns:
        LinkedList[int]: Sample linked list 5 -> 6 -> 7
    """
    linked_list = LinkedList[int]()

    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)

    return linked_list
