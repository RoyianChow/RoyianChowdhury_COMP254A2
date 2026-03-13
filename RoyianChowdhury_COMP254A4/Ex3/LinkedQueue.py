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
from contextlib import nullcontext

from Queue import Queue
from SinglyLinkedList import SinglyLinkedList


class LinkedQueue(Queue):
    """
     * Realization of a FIFO queue as an adaptation of a SinglyLinkedList.
     * All operations are performed in constant time.
     *
     * @author Michael T. Goodrich
     * @author Roberto Tamassia
     * @author Michael H. Goldwasser
     * @see SinglyLinkedList
    """

    def __init__(self):
        """ Constructs an initially empty queue. """
        self.list = SinglyLinkedList()   # an empty  list

    def size(self):
        """
         * Returns the number of elements in the queue.
         * @return number of elements in the queue
        """
        return self.list.size()

    def isEmpty(self):
        """
         * Tests whether the queue is empty.
         * @return true if the queue is empty, false otherwise
        """
        return self.list.isEmpty()

    def enqueue(self, element):
        """
         * Inserts an element at the rear of the queue.
         * @param element  the element to be inserted
        """
        self.list.addLast(element)

    def first(self):
        """
         * Returns, but does not remove, the first element of the queue.
         * @return the first element of the queue (or null if empty)
        """
        return self.list.first()

    def dequeue(self):
        """
         * Removes and returns the first element of the queue.
         * @return element removed (or null if empty)
        """
        return self.list.removeFirst()

    def concatenation(self, Q2):
        if Q2.isEmpty():
            return self
        if self.isEmpty():
            self.list.head = Q2.list.head
            self.list.tail = Q2.list.tail
            return self
        #check if either the first or second queue is empty
        else:
            self.list.tail.setNext(Q2.list.head)
            #connect tail to head
            self.list.tail = Q2.list.tail
            self.list.size_value += Q2.list.size_value
            #add the size value of q2 to self
            Q2.list.head = None
            Q2.list.tail = None
            Q2.list.size_value = 0
            #empty out q2

            return self


    def __str__(self):
        """
         * Produces a string representation of the contents of the queue.
         *  (from front to back). This exists for debugging purposes only.
        """
        return str(self.list)