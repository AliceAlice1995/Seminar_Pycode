# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числa вида 2k), 
# не превосходящие числа N.

n = int(input("Введите число: "))
numbers = []
i = 0

while 2 ** i <= n:
    numbers.append(2 ** i)
    i += 1

print(f"Все степени двойки заданного числа: {numbers}")


