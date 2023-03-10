# Задача 1: 
"""Написать программу, которая будет проверять пароль. Пусть программа в начале
запросит пароль у пользователя. В самой программе сохраните определенный пароль
и сравните его с тем, который был введен пользователем. В случае, если пароли
совпадают, то выведете на экран следующее сообщение: ‘Password is correct. You are
welcome’ Если нет: ‘Password is incorrect. Please, try again’
Программу решить 2 способами, 4 строчной if else конструкцией и 1 строчной версией
if else."""


# password = input("Please input Password: ")
# correct_password = "Hi"

# ## Первый способ
# if password == correct_password:
#     print('Password is correct. You are welcome')
# else:
#     print('Password is incorrect. Please, try again')

# ##Второй способ
# #print('Password is correct. You are welcome') if(password == correct_password) else print('Password is incorrect. Please, try again')

# Задача 2
"""Написать программу, которая будет спрашивать у пользователя температуру за окном.
Используя условные конструкции if elif else, напишите программу, которая выводит на
экран следующее:
1) При условии меньше -30 градусов: “Там так холодно, лучше дома сиди!”
2) При условии от -30 до 0: “Холодновато. Оденься потеплее!”
3) При условии от 0 до 15: “Прохладно. Куртку накинь!”
4) При условии от 15 до 30: “Тепло. Иди погуляй в парке!”
5) При условии от 30 до 50 включительно: “Ого, как жарко!”
6) При условии выше 50: “Там такая жара, лучше сиди дома!”
7) В других случаях: “Ошибка!”"""

# temperature = input("Введите температуру за окном в градусах Цельсия: ")  #Input data
# def is_number(temperature):         # Проверяем вводится число или другие символы (буквы, знаки)?
#     try:
#         float(temperature)
#         return True
#     except ValueError:
#         return False

# if is_number(temperature) == False:    #Если вводится не число, выдаётся ошибка
#         print("Ошибка!")
# else:
#     temperature = float(temperature)    #Если вводится числовое значение с типом str, преобразуем его во float для дальнейших вычислений
#     if temperature < -30:
#         print("Там так холодно, лучше дома сиди!") 
#     elif temperature >= -30 and temperature<0:
#         print("Холодновато. Оденься потеплее!")
#     elif temperature >= 0 and temperature<15:
#         print("Прохладно. Куртку накинь!")
#     elif temperature >= 15 and temperature<30:
#         print("Тепло. Иди погуляй в парке!")
#     elif temperature >= 30 and temperature <=50:
#         print("Ого, как жарко!")
#     elif temperature > 50:
#         print("Там такая жара, лучше сиди дома!")


# Задача 3
""" Вам дается текст:
Advertising companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children’s ‘pester
power’ to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money.
Посчитайте количество букв s и t ."""

text = '''Advertising companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children’s ‘pester
power’ to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money.'''

print("Number of letters 's' is: ", text.count('s'), "\nNumber of letters 't' is: ", text.count('t'))

# Дополнительное задание
"""Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную
строку из двух имен, буква за буквой.
Результат: "AAiddialneat"""

# str1="Aidana"                               #Вводим данные
# str2="Adilet"

# line_list1 = list(str1)                     #Перевод строки в список
# line_list2 = list(str2)

# comon_line = line_list1 + line_list2        # Объединение списков
# i=0;  k=0                                      # Определяем начальные индексы итераторов
# for i in range(len(comon_line)):            #Проход по объединённому списку с итератором для длинного слова
#     if i % 2==0:                            #Проверка на чётность элемента списка
#         comon_line[i]=line_list1[k]         #Если чётный или 0, берём элемент из первого списка
#     else:
#         comon_line[i]=line_list2[k]         #В противном случае - берём элемент из второго списка
#         k+=1                                #Увеличиваем индекс итератора для коротких слов
# print(''.join(str(n) for n in comon_line))  #Преобразуем список обратно в строку и выводим результат