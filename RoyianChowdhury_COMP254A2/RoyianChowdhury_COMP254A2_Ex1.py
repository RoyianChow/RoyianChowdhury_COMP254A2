#
# Source code recreated from a .class file by IntelliJ IDEA
# (powered by FernFlower decompiler)
#

class Exercises:
    @staticmethod
    def example1(arr):
        n = len(arr)
        total = 0

        for j in range(0, n):
            total += arr[j]

        return total
    #The is O(n) because the runtime is as long as n

    @staticmethod
    def example2(arr):
        n = len(arr)
        total = 0

        for j in range(0, n, 2):
            total += arr[j]

        return total
    #This is big 0(n/2) because the steps are by 2 so the runtime is cut in half

    @staticmethod
    def example3(arr):
        n = len(arr)
        total = 0

        for j in range(0, n):
            for k in range(0, j + 1):
                total += arr[j]

        return total
    #This is O(n^2) because for every time the loop runs once through n,
    # it runs through the entirety of n
    @staticmethod
    def example4(arr):
        n = len(arr)
        prefix = 0
        total = 0

        for j in range(0, n):
            prefix += arr[j]
            total += prefix

        return total
    #The is O(n) because the runtime is as long as n

    @staticmethod
    def example5(first, second):
        n = len(first)
        count = 0

        for i in range(0, n):
            total = 0

            for j in range(0, n):
                for k in range(0, j + 1):
                    total += first[k]

            if second[i] == total:
                count += 1

        return count
    #This is O(n^3) because for every time the loop runs once through n,
    # it runs through the entirety of n and does it again