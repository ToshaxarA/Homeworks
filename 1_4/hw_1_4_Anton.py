#Задание 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть
# пронумерована. Подсказка: Используйте функцию range() или enumerate()

# zeros = ['0000','0000','0000','0000','0000']
# for i, j in enumerate(zeros):
#     print(i,j)

#Задание 2. Нужно заполнить пустой список от 1 до 100. Полученный результат вывести на
# экран. Подсказка: используйте функцию range() и пустой список

# lst1 = []
# for i in range(1,101):
#     lst1.append(i)
# print(lst1)

#Задание 3. Вывести на экран все чётные значения в диапазоне от 1 до 497. Подсказка:
# используйте функцию range() или условия

# even=[]
# for i in range (1, 497):
#     if i%2 == 0:
#         even.append(i)
# print(even)

# Задание 4. 
"""Суммирование тысячи чисел: создайте список чисел от 1 до 1 000, затем
воспользуйтесь функциями min() и max() и убедитесь в том, что список действительно
начинается с 1 и заканчивается 1 000. Вызовите функцию sum() и посмотрите,
насколько быстро Python сможет просуммировать тысячу чисел"""
# import time 
# lst2 = []
# for i in range(1,1001):
#     lst2.append(i)
# print("Минимальное число в списке:", min(lst2))
# print("Максимальное число в списке:", max(lst2))
# start = time.time() ## точка отсчета времени
# sum(lst2)
# end = time.time() ## точка окончания работы программы
# time1 = end - start
# print(f'Время выполнения суммирования: {time1}', "сек")
# print("Сумма элементов в списке: ", sum(lst2))

#Задание 5. Заполнить список ста нулями с помощью функции range()
# lst3=[]
# k = 0
# for i in range(0,100):
#         lst3.append(k)
# print("Список: ", lst3)
# print("Число нулей в списке = ", lst3.count(0))

# Задание 6. Создайте кортеж it_company = (‘Google’, ‘Amazon’, ‘Microsoft’) вам нужно превратить
# кортеж в список и добавить новое значение ‘Tesla’, затем превращаете список обратно в кортеж

# it_company = ('Google', 'Amazon', 'Microsoft')
# lst4 = list(it_company)  # Преобразование в список
# print(lst4)
# lst4.append('Tesla')     # Преобразование в кортеж
# print(tuple(lst4))


# Задание 7. Из 6 задания попробуйте вывести индекс ‘Amazon’.
# it_company = ('Google', 'Amazon', 'Microsoft')
# print(it_company[1])

# Задание 8. Из 6 задания обновите значение ‘Google’ на ‘Apple’ любыми способами.
# it_company = ('Google', 'Amazon', 'Microsoft')
# lst4 = list(it_company)  # Преобразование в список
# lst4[0]="Apple"
# print(tuple(lst4))


# Задание 9. Из 1 задания сделайте срез ‘Apple’ до ‘Microsoft’

# it_company = ('Google', 'Amazon', 'Microsoft')
# lst4 = list(it_company)  # Преобразование в список
# lst4[0]="Apple"
# tuple(lst4)
# print(lst4[0:2])

# Задание 10. Есть кортеж text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
# 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
# 'overview') вам нужно посчитать сколько раз встречается слово python.

# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
# 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
# 'overview')
# print("Слово 'python' встречается в кортеже ",text_tuple.count('python'), "раз")  # python встречается в кортеже 0 раз
# print("Слово 'Python' встречается в кортеже ",text_tuple.count('Python'), "раза") # Python встречается в кортеже 0 раз


# Дополнительное задание 6. Исходные значения двух переменных запросить у пользователя. Поменять значения
# переменных местами. Вывести новые значения на экран. Решите задачу, используя только две переменные.
# a = input("Введите занчение переменной №1: ")
# b = input("Введите занчение переменной №2: ")
# a, b = b, a
# print(a, b)

# Дополнительное задание 7. Создайте бесконечный цикл. Запросите у пользователя его возраст. Если ему есть
# 18 лет, выведите: "Доступ разрешен" и остановите цикл, иначе "Извините, пользование
# данным ресурсом только с 18 лет" и запросите заново.

def out_red(text):
    print("\033[31m {}" .format(text))
def out_green(text):
    print("\033[32m {}" .format(text))
def out_white(text):
    print("\033[37m {}" .format(text))

while True:
    age = int(input("Сколько Вам лет? "))
    if age>=18:
        out_green("Доступ разрешен")
        out_white("")
        break
    else:
        out_red("Извините, пользование данным ресурсом только с 18 лет")
        out_white("")