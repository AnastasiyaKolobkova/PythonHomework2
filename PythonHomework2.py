# Домашняя работа 2.
# Задача 1.
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет лежащих на столе: '))
m = 0
for i in range(n):
    a = int(input('Введите какой стороной лежит монета: решка - 1, герб - 0: '))
    if a == 1:
        m += 1
print(m if m<n/2 else n-m)

# Задача 2.
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

a = int(input('Введите сумму загаданных чисел: '))
b = int(input('Введите произведение загаданных чисел: '))
for i in range(a):
    for j in range(b):
        if i + j == a and i * j == b:
            print(f'Первое число: {i}, второе число: {j}')

# Задача 3.
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
m = 1
while m < n:
    print(m, end=' ')
    m = m * 2