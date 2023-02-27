# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

import math


def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n, m = int(line[0]), int(line[1])
    a = set()
    b = set()
    arr = []
    for i in range((10 ** 5) + 1):
        arr.append(0)
    line = input_file.readline().split()
    for i in range(n):
        a.add(int(line[i]))
    line = input_file.readline().split()
    for i in range(m):
        b.add(int(line[i]))
    for i in a:
        arr[i] += 1
    for i in b:
        arr[i] += 1
    mass = []
    for i in range(len(arr)):
        if arr[i] > 1:
            mass.append(i)
    print(mass)
