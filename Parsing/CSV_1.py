import csv
import collections
"""считывает преступления из файла, записывает в список категорию преступлений, удаляет первый элемент - это 
название колонки, выводит на экран самое часто совершаемое преступление и количество"""
lst = []
with open("d:\\crimes.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        lst.append(row[5])
del lst[0]
c = collections.Counter(lst).most_common(1)

for i in range(len(c[0])):
    print(c[0][i], end=' ')




