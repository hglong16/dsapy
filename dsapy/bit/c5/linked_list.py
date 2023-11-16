from dsapy.libs.linked_list import LinkedList

if __name__ == "__main__":
    linked_list = LinkedList[int]()
    linked_list.push(5)
    linked_list.push(6)

    print(linked_list)
