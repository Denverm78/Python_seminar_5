# Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

# gen = (item for item in (range(2, 101, 2)))
# for i in gen:
# if sum(int(j) for j in str(i)) != 8:
# print(i)


# print([i for i in (i for i in (range(2, 101, 2)) if sum(int(j) for j in str(i)) != 8)])

for i in (i for i in (range(2, 101, 2)) if sum(int(j) for j in str(i)) != 8):
    print(i)
