from random import random

"""def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    yield 2
    print('Check 3')

gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(y)
z = next(gen)"""


class RandomIterator:

    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


def random_generator(k):
    for _ in range(k):
        yield random()


gen = random_generator(10)
for i in gen:
    print(i)

"""class DoubleElementListIterator:
    
    
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


for pair in MyList([1, 2, 3, 4, 5]):
    print(pair)"""
