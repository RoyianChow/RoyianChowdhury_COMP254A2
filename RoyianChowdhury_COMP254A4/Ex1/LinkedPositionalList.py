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

from Position import Position
from PositionalList import PositionalList


class LinkedPositionalList(PositionalList):
    """
     * Implementation of a positional list stored as a doubly linked list.
     *
     * @author Michael T. Goodrich
     * @author Roberto Tamassia
     * @author Michael H. Goldwasser
    """

    # ---------------- nested Node class ----------------
    class Node(Position):
        """
         * Node of a doubly linked list, which stores a reference to its
         * element and to both the previous and next node in the list.
        """

        def __init__(self, e, p, n):
            """
             * Creates a node with the given element and next node.
             *
             * @param e  the element to be stored
             * @param p  reference to a node that should precede the new node
             * @param n  reference to a node that should follow the new node
            """
            self.element = e
            self.prev = p
            self.next = n

        # public accessor methods
        def getElement(self):
            """
             * Returns the element stored at the node.
             * @return the stored element
             * @throws IllegalStateException if node not currently linked to others
            """
            if self.next is None:  # convention for defunct node
                raise Exception("Position no longer valid")
            return self.element

        def getPrev(self):
            """
             * Returns the node that precedes this one (or null if no such node).
             * @return the preceding node
            """
            return self.prev

        def getNext(self):
            """
             * Returns the node that follows this one (or null if no such node).
             * @return the following node
            """
            return self.next

        # Update methods
        def setElement(self, e):
            """
             * Sets the node's element to the given element e.
             * @param e    the node's new element
            """
            self.element = e

        def setPrev(self, p):
            """
             * Sets the node's previous reference to point to Node n.
             * @param p    the node that should precede this one
            """
            self.prev = p

        def setNext(self, n):
            """
             * Sets the node's next reference to point to Node n.
             * @param n    the node that should follow this one
            """
            self.next = n

    # instance variables of the LinkedPositionalList
    def __init__(self):
        """ Constructs a new empty list. """
        self.header = self.Node(None, None, None)     # create header
        self.trailer = self.Node(None, self.header, None)  # trailer is preceded by header
        self.header.setNext(self.trailer)             # header is followed by trailer
        self.size_value = 0                           # number of elements in the list

    # private utilities
    def validate(self, p):
        """
         * Verifies that a Position belongs to the appropriate class, and is
         * not one that has been previously removed. Note that our current
         * implementation does not actually verify that the position belongs
         * to this particular list instance.
         *
         * @param p   a Position (that should belong to this list)
         * @return    the underlying Node instance at that position
         * @throws IllegalArgumentException if an invalid position is detected
        """
        if not isinstance(p, self.Node):
            raise Exception("Invalid p")
        node = p  # safe cast
        if node.getNext() is None:  # convention for defunct node
            raise Exception("p is no longer in the list")
        return node

    def position(self, node):
        """
         * Returns the given node as a Position, unless it is a sentinel, in which case
         * null is returned (so as not to expose the sentinels to the user).
        """
        if node == self.header or node == self.trailer:
            return None  # do not expose user to the sentinels
        return node

    # public accessor methods
    def size(self):
        """
         * Returns the number of elements in the list.
         * @return number of elements in the list
        """
        return self.size_value

    def isEmpty(self):
        """
         * Tests whether the list is empty.
         * @return true if the list is empty, false otherwise
        """
        return self.size_value == 0

    def first(self):
        """
         * Returns the first Position in the list.
         *
         * @return the first Position in the list (or null, if empty)
        """
        return self.position(self.header.getNext())

    def last(self):
        """
         * Returns the last Position in the list.
         *
         * @return the last Position in the list (or null, if empty)
        """
        return self.position(self.trailer.getPrev())

    def before(self, p):
        """
         * Returns the Position immediately before Position p.
         * @param p   a Position of the list
         * @return the Position of the preceding element (or null, if p is first)
         * @throws IllegalArgumentException if p is not a valid position for this list
        """
        node = self.validate(p)
        return self.position(node.getPrev())

    def after(self, p):
        """
         * Returns the Position immediately after Position p.
         * @param p   a Position of the list
         * @return the Position of the following element (or null, if p is last)
         * @throws IllegalArgumentException if p is not a valid position for this list
        """
        node = self.validate(p)
        return self.position(node.getNext())

    # private utilities
    def addBetween(self, e, pred, succ):
        """
         * Adds an element to the linked list between the given nodes.
         * The given predecessor and successor should be neighboring each
         * other prior to the call.
         *
         * @param pred     node just before the location where the new element is inserted
         * @param succ     node just after the location where the new element is inserted
         * @return the new element's node
        """
        newest = self.Node(e, pred, succ)  # create and link a new node
        pred.setNext(newest)
        succ.setPrev(newest)
        self.size_value += 1
        return newest

    # public update methods
    def addFirst(self, e):
        """
         * Inserts an element at the front of the list.
         *
         * @param e the new element
         * @return the Position representing the location of the new element
        """
        return self.addBetween(e, self.header, self.header.getNext())  # just after the header

    def addLast(self, e):
        """
         * Inserts an element at the back of the list.
         *
         * @param e the new element
         * @return the Position representing the location of the new element
        """
        return self.addBetween(e, self.trailer.getPrev(), self.trailer)  # just before the trailer

    def addBefore(self, p, e):
        """
         * Inserts an element immediately before the given Position.
         *
         * @param p the Position before which the insertion takes place
         * @param e the new element
         * @return the Position representing the location of the new element
         * @throws IllegalArgumentException if p is not a valid position for this list
        """
        node = self.validate(p)
        return self.addBetween(e, node.getPrev(), node)

    def addAfter(self, p, e):
        """
         * Inserts an element immediately after the given Position.
         *
         * @param p the Position after which the insertion takes place
         * @param e the new element
         * @return the Position representing the location of the new element
         * @throws IllegalArgumentException if p is not a valid position for this list
        """
        node = self.validate(p)
        return self.addBetween(e, node, node.getNext())

    def set(self, p, e):
        """
         * Replaces the element stored at the given Position and returns the replaced element.
         *
         * @param p the Position of the element to be replaced
         * @param e the new element
         * @return the replaced element
         * @throws IllegalArgumentException if p is not a valid position for this list
        """
        node = self.validate(p)
        answer = node.getElement()
        node.setElement(e)
        return answer

    def remove(self, p):
        """
         * Removes the element stored at the given Position and returns it.
         * The given position is invalidated as a result.
         *
         * @param p the Position of the element to be removed
         * @return the removed element
         * @throws IllegalArgumentException if p is not a valid position for this list
        """
        node = self.validate(p)
        predecessor = node.getPrev()
        successor = node.getNext()
        predecessor.setNext(successor)
        successor.setPrev(predecessor)
        self.size_value -= 1
        answer = node.getElement()
        node.setElement(None)   # help with garbage collection
        node.setNext(None)      # and convention for defunct node
        node.setPrev(None)
        return answer

    # support for iterating either positions and elements
    # ---------------- nested PositionIterator class ----------------
    class PositionIterator:
        """
         * A (nonstatic) inner class. Note well that each instance
         * contains an implicit reference to the containing list,
         * allowing us to call the list's methods directly.
        """

        def __init__(self, outer):
            self.outer = outer
            self.cursor = outer.first()   # position of the next element to report
            self.recent = None            # position of last reported element

        def hasNext(self):
            """
             * Tests whether the iterator has a next object.
             * @return true if there are further objects, false otherwise
            """
            return self.cursor is not None

        def next(self):
            """
             * Returns the next position in the iterator.
             *
             * @return next position
             * @throws NoSuchElementException if there are no further elements
            """
            if self.cursor is None:
                raise Exception("nothing left")
            self.recent = self.cursor
            self.cursor = self.outer.after(self.cursor)
            return self.recent

        def remove(self):
            """
             * Removes the element returned by most recent call to next.
             * @throws IllegalStateException if next has not yet been called
             * @throws IllegalStateException if remove was already called since recent next
            """
            if self.recent is None:
                raise Exception("nothing to remove")
            self.outer.remove(self.recent)
            self.recent = None

        def __iter__(self):
            return self

        def __next__(self):
            if not self.hasNext():
                raise StopIteration
            return self.next()

    # ---------------- nested PositionIterable class ----------------
    class PositionIterable:
        def __init__(self, outer):
            self.outer = outer

        def __iter__(self):
            return LinkedPositionalList.PositionIterator(self.outer)

    def positions(self):
        """
         * Returns an iterable representation of the list's positions.
         * @return iterable representation of the list's positions
        """
        return self.PositionIterable(self)

    # ---------------- nested ElementIterator class ----------------
    class ElementIterator:
        """ This class adapts the iteration produced by positions() to return elements. """

        def __init__(self, outer):
            self.posIterator = LinkedPositionalList.PositionIterator(outer)

        def hasNext(self):
            return self.posIterator.hasNext()

        def next(self):
            return self.posIterator.next().getElement()  # return element!

        def remove(self):
            self.posIterator.remove()

        def __iter__(self):
            return self

        def __next__(self):
            if not self.hasNext():
                raise StopIteration
            return self.next()

    def iterator(self):
        """
         * Returns an iterator of the elements stored in the list.
         * @return iterator of the list's elements
        """
        return self.ElementIterator(self)

    def __iter__(self):
        return self.iterator()

    # Debugging code
    def __str__(self):
        """
         * Produces a string representation of the contents of the list.
         * This exists for debugging purposes only.
        """
        sb = "("
        walk = self.header.getNext()
        while walk != self.trailer:
            sb += str(walk.getElement())
            walk = walk.getNext()
            if walk != self.trailer:
                sb += ", "
        sb += ")"
        return sb

    def indexOf(self, p):
        current = self.first()
        index = 0
        while current is not None:
            if current == p:
                return index
            current = self.after(current)
            index += 1
        return -1

