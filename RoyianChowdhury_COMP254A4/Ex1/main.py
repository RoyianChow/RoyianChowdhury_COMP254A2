import LinkedPositionalList

if __name__ == "__main__":
    pList = LinkedPositionalList.LinkedPositionalList()
    p1=pList.addFirst(1)
    p2=pList.addLast(2)
    p3=pList.addLast(3)
    p4=pList.addLast(4)
    print(pList.indexOf(p3))
