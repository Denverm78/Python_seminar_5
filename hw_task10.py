# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonaci(n):
    number1 = 0
    number2 = 1
    for i in range(n-2):
        number3 = number1 + number2
        number1, number2 = number2, number3        
        yield number3

num = int(input("Введите количество чисел Фибоначи для вывода: "))
print("Числа Фибоначи: ")
if num == 1:
    print(1,') ',0)
else:
    print(1,') ',0)
    print(2,') ',1)
    for i, num in enumerate(fibonaci(num), start=3):
        print(i,') ',num)   