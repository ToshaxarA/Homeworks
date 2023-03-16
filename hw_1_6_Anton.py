# Задание 1. Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- # FYI и т.п.

# def capital(fraze:str) ->str:
#     ful_fraze=input("Введите фразу: ")
#     short_fraze = []
#     ful_fraze=ful_fraze.title()
#     for i in range(len(ful_fraze)):
#         if ful_fraze[i].isupper() == True:
#             short_fraze.append(ful_fraze[i])
#     print("".join(short_fraze))
# capital(1)

# Задание 2. Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
# фразе было использовано. Например: “Money, money, money, it’s always sunny, in the richmen’s world”.
#  money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1

# def words_counter(fraze:str):
#     text = input("Введите фразу: ")
#     text = text.replace("\n", " ")  #Замена переносов на пробелы
#     text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "") #Замена знаков пунктуации на пробелы
#     text = text.lower()      # Все слова начинаются с маленькой буквы
#     words = text.split() # Разделение строки по разделителю, пробел по умолчанию
#     # print(words)
#     words_dict = dict()     #Создание пустого словаря 
#     for word in words:      
#         if word in words_dict:
#             words_dict[word] = words_dict[word] + 1
#         else:
#             words_dict[word] = 1
#     print(words_dict)    
# words_counter(1)

def count_words(word:str):
    word_split = word.lower().replace(',','').split()
    res ={}
    for n in word_split:
        # print(word_split.count(n))
        res[n]=word_split.count(n)
    return res
# return word_split
# count_words("Money, money, money, it's always sunny, in the richmen's world")
print(count_words("Money, money, money, it's always sunny, in the richmen's world"))

# Задание 3. 
# Напишите функцию, которая принимает слово и возвращает True, если слово
# изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.
    
# def izogram(slovo:str) -> bool:
#     cache = {}
#     slovo = input("Введите слово: ") 
#     for char in slovo:
#         lowerChar = char.lower()
#         if not lowerChar in cache: 
#             cache[lowerChar] = True
#             print(cache)
#         else:
#             print('False')
#             return False
#     print('True')
#     return True
# izogram(1)

# #3.1
# def isogramma(word):
#     return True if len(word) == len(set(word)) else False
# #3.2
# print((lambda word: True if len(word) == len(set(word)) else False)('hello'))
    
            

# Задание 4. Напишите функцию где мы передаем через аргументы число n как целое
# integer, надо вывести целое число в перевернутом виде например: n = 27, тогда перевёрнутое n это 72.

# def perestanovka(num:int):
#     number = int(input("Введите целое число: "))
#     num2 = 0
 
#     while number > 0:
#     # находим остаток - последнюю цифру
#         digit = number % 10
#     # делим нацело - удаляем последнюю цифру
#         number = number // 10
#     # увеличиваем разрядность второго числа и добавляем очередную цифру
#         num2 = num2 * 10 + digit  
#     print('"Обратное" число:', num2)
# perestanovka(1)


# def reverser_int(num:int = 23) -> int:
#     return int(str(num)[::-1])
# print(reverser_int(27))



# Дополнтиельное задание 5. Напишите функцию -- чат-бот с бесконечным циклом, который
# a. Всегда отвечает “Конечно!” на любой вопрос
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же духе!” 
# Если вызвал функцию, но ничего не передал.
# d. В любых других случаях, отвечает “ну и что”

# def chatbot(question:str) ->str:
#     while True:
#         question = input("Задайте вопрос: ")
#         if question == '':
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         elif question == question.upper() and "!" in question:
#             print("Успокойся")
#         elif "?" in question:
#             print("Конечно!")
#         else:
#             print("ну и что")
# chatbot(1)