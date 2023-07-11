# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def func_split_path(full_path):
    *split_path, name_with_extension = full_path.split('\\')
    path = '\\'.join(split_path) + '\\'
    *split_name, extension = name_with_extension.split('.')
    name = '.'.join(split_name)
    result = (path, name, extension)
    return result

file_path = 'C:\Program Files\Java\jdk-17.0.5\legal\java.rmi'
print('Исходный путь: ', file_path)
print('Итоговый кортеж: ', func_split_path(file_path))
