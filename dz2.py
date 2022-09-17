# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

spisok = list(map(int,input('введите числа списка через пробел: ').split()))
listLength = 0
if len(spisok) % 2 == 0:
    listLength = len(spisok) // 2
else:
    listLength = len(spisok) // 2 + 1
for i in range (listLength):
    print(spisok[i] * spisok[len(spisok) - 1 - i])