class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # addFirst
    def add_first(self, element):
        new_node = Node(element, self.head)
        self.head = new_node
        self.size += 1

    # addLast (no tail used → must traverse)
    def add_last(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
        else:
            walk = self.head
            while walk.next is not None:
                walk = walk.next
            walk.next = new_node

        self.size += 1

    # concatenate two singly linked lists
    # input: L1, L2
    # output: concatenated list (returns L1)
    def concatenate_lists(self, L1, L2):

        if L1.head is None:
            return L2

        walk = L1.head  # point to head of L1

        # traverse L1
        while walk.next is not None:
            walk = walk.next

        # link to head of L2
        walk.next = L2.head

        return L1

    # secondToLast (same as your Java version)
    def second_to_last(self):
        if self.size < 2:
            raise Exception("List must have 2 or more elements")

        walk = self.head
        while walk.next.next is not None:
            walk = walk.next

        return walk

    # for printing
    def __str__(self):
        elements = []
        walk = self.head
        while walk is not None:
            elements.append(str(walk.element))
            walk = walk.next
        return " -> ".join(elements) + " -> None"


# ------------------ MAIN ------------------

if __name__ == "__main__":

    list1 = SinglyLinkedList()
    list1.add_first("MSP")
    list1.add_last("ATL")
    list1.add_last("BOS")

    list2 = SinglyLinkedList()
    list2.add_first("YYZ")
    list2.add_last("MTRL")
    list2.add_last("OTW")

    print("List1:", list1)
    print("List2:", list2)

    list1.concatenate_lists(list1, list2)

    print("Concatenated:", list1)

    print("Second to last:", list1.second_to_last().element)