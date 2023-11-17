from dsapy.libs.utils.utils import create_linked_list

if __name__ == "__main__":
    linked_list = create_linked_list()

    while not linked_list.is_empty:
        print(linked_list.remove_last())
