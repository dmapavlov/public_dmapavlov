from itertools import takewhile
import itertools


def primes():
    n = 1000
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j += i
        i += 1
    a = set(a)
    a.remove(0)
    for i in sorted(a):
        yield i


print(list(itertools.takewhile(lambda x: x <= 1000, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
