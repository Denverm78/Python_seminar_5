# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.

def gen_dict_salary(names, salary, percent):
    dict_salary = ({name : salary * float(percent[:-1]) / 100 
                   for name, salary, percent in zip(names, salary, percent)})
    return dict_salary


names_list = ["Егор", "Светлана", "Денис", "Анна"]
salary_list = [30000, 32000, 35000, 25000]
percent_list = ['10.25%', '10.50%', '15.50%', '12.00%']
result_dict = gen_dict_salary(names_list, salary_list, percent_list)
print()
print("Итоговый словарь c премиями:")
print(result_dict)
print() 