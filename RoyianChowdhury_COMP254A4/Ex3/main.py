from LinkedQueue import LinkedQueue

if __name__ == "__main__":
    q1 = LinkedQueue()
    q2 = LinkedQueue()

    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    q2.enqueue(5)
    q2.enqueue(6)
    q2.enqueue(7)
    print(q1)
    q1.concatenation(q2)
    print(q1)
    print(q2)
    pass