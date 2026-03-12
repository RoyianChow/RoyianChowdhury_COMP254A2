
from singlyLinkedList import SinglyLinkedList as sl


def concat(list1, list2):
    walk = list1.head
    while walk.next != None:
        walk = walk.next
    walk.next = list2.head
    return list1

if __name__ == "__main__":
    l1 = sl()
    l1.add_first(1)
    l1.add_last(2)
    l1.add_last(3)
    l1.add_last(4)
    l1.add_last(5)
    l1.add_last(6)
    l2 = sl()
    l2.add_first(7)
    l2.add_last(8)
    l2.add_last(9)
    l2.add_last(10)

    print(concat(l1,l2))


