# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, 
# если делится нацело только на единицу и на себя».

def gen_prime_number(number):
    x=1
    while number > 0:
        x+=1
        for i in range(2, int(x//2+1)):
            if x % i == 0:
               x = x+1
               break
        number -= 1
        yield x



n = int(input("Введите количество простых чисел: "))
for i, num in enumerate(gen_prime_number(n), start=1):
        print(i,') ',num)