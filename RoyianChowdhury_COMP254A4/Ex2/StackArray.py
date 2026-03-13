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

from Stack import Stack


class ArrayStack(Stack):
    """
     * Implementation of the stack ADT using a fixed-length array.  All
     * operations are performed in constant time. An exception is thrown
     * if a push operation is attempted when the size of the stack is
     * equal to the length of the array.
     *
     * @author Michael T. Goodrich
     * @author Roberto Tamassia
     * @author Michael H. Goldwasser
    """

    CAPACITY = 1000   # default array capacity

    def __init__(self, capacity=None):
        """ Constructs an empty stack using the default array capacity. """
        if capacity is None:
            capacity = self.CAPACITY
        self.data = [None] * capacity
        self.t = -1

    def size(self):
        """
         * Returns the number of elements in the stack.
         * @return number of elements in the stack
        """
        return self.t + 1

    def isEmpty(self):
        """
         * Tests whether the stack is empty.
         * @return true if the stack is empty, false otherwise
        """
        return self.t == -1

    def push(self, e):
        """
         * Inserts an element at the top of the stack.
         * @param e   the element to be inserted
         * @throws IllegalStateException if the array storing the elements is full
        """
        if self.size() == len(self.data):
            raise Exception("Stack is full")
        self.t += 1
        self.data[self.t] = e

    def top(self):
        """
         * Returns, but does not remove, the element at the top of the stack.
         * @return top element in the stack (or null if empty)
        """
        if self.isEmpty():
            return None
        return self.data[self.t]

    def pop(self):
        """
         * Removes and returns the top element from the stack.
         * @return element removed (or null if empty)
        """
        if self.isEmpty():
            return None
        answer = self.data[self.t]
        self.data[self.t] = None
        self.t -= 1
        return answer

    def __str__(self):
        """
         * Produces a string representation of the contents of the stack.
         * (ordered from top to bottom). This exists for debugging purposes only.
         *
         * @return textual representation of the stack
        """
        sb = "("
        for j in range(self.t, -1, -1):
            sb += str(self.data[j])
            if j > 0:
                sb += ", "
        sb += ")"
        return sb


if __name__ == "__main__":
    S = ArrayStack()              # contents: ()
    S.push(5)                     # contents: (5)
    S.push(3)                     # contents: (5, 3)
    print(S.size())               # contents: (5, 3)     outputs 2
    print(S.pop())                # contents: (5)        outputs 3
    print(S.isEmpty())            # contents: (5)        outputs false
    print(S.pop())                # contents: ()         outputs 5
    print(S.isEmpty())            # contents: ()         outputs true
    print(S.pop())                # contents: ()         outputs null
    S.push(7)                     # contents: (7)
    S.push(9)                     # contents: (7, 9)
    print(S.top())                # contents: (7, 9)     outputs 9
    S.push(4)                     # contents: (7, 9, 4)
    print(S.size())               # contents: (7, 9, 4)  outputs 3
    print(S.pop())                # contents: (7, 9)     outputs 4
    S.push(6)                     # contents: (7, 9, 6)
    S.push(8)                     # contents: (7, 9, 6, 8)
    print(S.pop())                # contents: (7, 9, 6)  outputs 8