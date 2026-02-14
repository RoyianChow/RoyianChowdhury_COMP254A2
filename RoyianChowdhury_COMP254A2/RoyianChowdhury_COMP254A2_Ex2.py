import time
import matplotlib.pyplot as plt
import random


class PrefixAverage:

    # Returns an array a such that, for all j, a[j] equals the average of x[0], ..., x[j].
    @staticmethod
    def prefixAverage1(x):
        n = len(x)
        a = [0.0] * n  # filled with zeros by default
        for j in range(0, n):
            total = 0.0  # begin computing x[0] + ... + x[j]
            for i in range(0, j + 1):
                total += x[i]
            a[j] = total / (j + 1)  # record the average
        return a

    # Returns an array a such that, for all j, a[j] equals the average of x[0], ..., x[j].
    @staticmethod
    def prefixAverage2(x):
        n = len(x)
        a = [0.0] * n  # filled with zeros by default
        total = 0.0    # compute prefix sum as x[0] + x[1] + ...
        for j in range(0, n):
            total += x[j]           # update prefix sum to include x[j]
            a[j] = total / (j + 1)  # compute average based on current sum
        return a

    if __name__ == "__main__":
        ns = [1, 3, 9, 12, 15, 18, 21,100,1000,10000]
        times1 = []
        times2 = []
        for n in ns:
            arr = [random.random() for _ in range(n)]
            start = time.perf_counter()
            prefixAverage1(arr)
            end = time.perf_counter()
            times1.append(end - start)

            start = time.perf_counter()
            prefixAverage2(arr)
            end = time.perf_counter()
            times2.append(end - start)

        print("times1:", times1)
        print("times2:", times2)

        plt.figure()
        plt.loglog(ns, times1, marker='o', label="Prefix Average")
        plt.loglog(ns, times2,marker='o',  label="Prefix Average 2")
        plt.legend()
        plt.show()