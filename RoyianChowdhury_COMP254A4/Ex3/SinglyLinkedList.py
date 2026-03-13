"""
 * Copyright 2014, Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser
 *
 * Developed for use with the book:
 *
 *    Data Structures and Algorithms in Java, Sixth Edition
 *    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
 *    John Wiley & Sons, 2014
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import copy


class SinglyLinkedList:
    """
     * A basic singly linked list implementation.
     *
     * @author Michael T. Goodrich
     * @author Roberto Tamassia
     * @author Michael H. Goldwasser
    """

    class Node:
        """
         * Node of a singly linked list, which stores a reference to its
         * element and to the subsequent node in the list (or null if this
         * is the last node).
        """

        def __init__(self, e, n):
            """
             * Creates a node with the given element and next node.
             *
             * @param e  the element to be stored
             * @param n  reference to a node that should follow the new node
            """
            self.element = e
            self.next = n

        def getElement(self):
            """
             * Returns the element stored at the node.
             * @return the element stored at the node
            """
            return self.element

        def getNext(self):
            """
             * Returns the node that follows this one (or null if no such node).
             * @return the following node
            """
            return self.next

        def setNext(self, n):
            """
             * Sets the node's next reference to point to Node n.
             * @param n    the node that should follow this one
            """
            self.next = n

    def __init__(self):
        """ Constructs an initially empty list. """
        self.head = None               # head node of the list (or null if empty)
        self.tail = None               # last node of the list (or null if empty)
        self.size_value = 0            # number of nodes in the list

    def size(self):
        """
         * Returns the number of elements in the linked list.
         * @return number of elements in the linked list
        """
        return self.size_value

    def isEmpty(self):
        """
         * Tests whether the linked list is empty.
         * @return true if the linked list is empty, false otherwise
        """
        return self.size_value == 0

    def first(self):
        """
         * Returns (but does not remove) the first element of the list
         * @return element at the front of the list (or null if empty)
        """
        if self.isEmpty():
            return None
        return self.head.getElement()

    def last(self):
        """
         * Returns (but does not remove) the last element of the list.
         * @return element at the end of the list (or null if empty)
        """
        if self.isEmpty():
            return None
        return self.tail.getElement()

    def addFirst(self, e):
        """
         * Adds an element to the front of the list.
         * @param e  the new element to add
        """
        self.head = self.Node(e, self.head)
        if self.size_value == 0:
            self.tail = self.head
        self.size_value += 1

    def addLast(self, e):
        """
         * Adds an element to the end of the list.
         * @param e  the new element to add
        """
        newest = self.Node(e, None)
        if self.isEmpty():
            self.head = newest
        else:
            self.tail.setNext(newest)
        self.tail = newest
        self.size_value += 1

    def removeFirst(self):
        """
         * Removes and returns the first element of the list.
         * @return the removed element (or null if empty)
        """
        if self.isEmpty():
            return None
        answer = self.head.getElement()
        self.head = self.head.getNext()
        self.size_value -= 1
        if self.size_value == 0:
            self.tail = None
        return answer

    def __eq__(self, o):
        if o is None:
            return False
        if self.__class__ != o.__class__:
            return False
        other = o
        if self.size_value != other.size_value:
            return False
        walkA = self.head
        walkB = other.head
        while walkA is not None:
            if walkA.getElement() != walkB.getElement():
                return False
            walkA = walkA.getNext()
            walkB = walkB.getNext()
        return True

    def clone(self):
        other = copy.copy(self)
        if self.size_value > 0:
            other.head = self.Node(self.head.getElement(), None)
            walk = self.head.getNext()
            otherTail = other.head
            while walk is not None:
                newest = self.Node(walk.getElement(), None)
                otherTail.setNext(newest)
                otherTail = newest
                walk = walk.getNext()
            other.tail = otherTail
        return other

    def __hash__(self):
        h = 0
        walk = self.head
        while walk is not None:
            h ^= hash(walk.getElement())
            h = ((h << 5) | (h >> 27))
            walk = walk.getNext()
        return h

    def __str__(self):
        """
         * Produces a string representation of the contents of the list.
         * This exists for debugging purposes only.
        """
        sb = "("
        walk = self.head
        while walk is not None:
            sb += str(walk.getElement())
            if walk != self.tail:
                sb += ", "
            walk = walk.getNext()
        sb += ")"
        return sb