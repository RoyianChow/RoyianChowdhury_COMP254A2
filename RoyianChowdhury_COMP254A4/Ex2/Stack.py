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

from abc import ABC, abstractmethod


class Stack(ABC):
    """
     * A collection of objects that are inserted and removed according to the last-in
     * first-out principle. Although similar in purpose, this interface differs from
     * java.util.Stack.
     *
     * @author Michael T. Goodrich
     * @author Roberto Tamassia
     * @author Michael H. Goldwasser
    """

    @abstractmethod
    def size(self):
        """
         * Returns the number of elements in the stack.
         * @return number of elements in the stack
        """
        pass

    @abstractmethod
    def isEmpty(self):
        """
         * Tests whether the stack is empty.
         * @return true if the stack is empty, false otherwise
        """
        pass

    @abstractmethod
    def push(self, e):
        """
         * Inserts an element at the top of the stack.
         * @param e   the element to be inserted
        """
        pass

    @abstractmethod
    def top(self):
        """
         * Returns, but does not remove, the element at the top of the stack.
         * @return top element in the stack (or null if empty)
        """
        pass

    @abstractmethod
    def pop(self):
        """
         * Removes and returns the top element from the stack.
         * @return element removed (or null if empty)
        """
        pass