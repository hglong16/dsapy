from dsapy.libs.utils.utils import create_linked_list

if __name__ == "__main__":
    linked_list = create_linked_list()
    linked_list.append(8)
    linked_list.append(9)
    linked_list.append(10)

    slow = linked_list.head
    fast = linked_list.head  # go double speed with slow

    while (fast is not None) and (fast.next.next is not None):
        slow = slow.next  # type: ignore
        fast = fast.next.next

    print(linked_list)
    print(slow.value)  # type: ignore
