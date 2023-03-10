#Циклы for, while
# print(1)
# print(2)
# print(3)
# print(4)

# for i in range(1, 1000, 2):
#     print(i)

# cars = ["BMW", "TOYOTA", "MERCEDES", "HONDA"]
# print(cars)
# for car in cars:
#     if "MERCEDES" == car:
#         print(True)
#     else:
#         print(False)

# numbers = [10, 1, 3, 5, 100, 101, 500, 111, 113, 403, 607, 809, 901, 307]
# for num in numbers:
#     if num % 2 == 0:
#         print(num, "четный")
#     else:
#         print(num, "нечетный")

# nums = []
# for n in range(1, 101):
#     nums.append(n)
#     if n == 70:
#         print("STOP")
#         continue
# print(nums)

# it = "Geeks Python"
# for i in it:
#     print(i)

# tup = (101, 400.6, True, "Hello", [10, 20, 30])
# for t in tup:
#     print(t)

# num = '1001'
# for n in num:
#     print(n)

# import random
# # print(random.randint(1, 10))
# # names = ["Nurbolot", "Askhat", "Nurtilek", "Anton"]
# # print(random.choice(names))

# password_generator = "qwertyuioopasdfghjklzxcvbnm1234567890@#$%^&*"
# how_many_password = int(input("Сколько паролей вам нужно: "))
# len_password = int(input("Длина паролей: "))
# for j in range(how_many_password):
#     res = ""
#     for i in range(len_password):
#         choice = random.choice(password_generator)
#         # res = res + choice
#         res += choice
#     print(res)

# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 += 1
#     print(num1)

# n = 0
# while True:
#     n += 1
#     print(n, "Geeks")
    # if n == 100:
    #     print("STOP")
    #     break

# import random
# password = random.randint(1111, 9999)
# print(password)
# n = 1111
# while True:
#     print(n)
#     if password == n:
#         print(n, "is password")
#         break
#     n += 1

# for i in range(10, 100, 2):
#     print(i)

# start = 10
# end = 100
# step = 2
# while True:
#     print(start)
#     start += step
#     if start == end:
#         break

# import requests

# res = requests.get("https://kyzmat24.com/api/users").json()
# for r in res:
#     # print(r['username'])
#     if r['username'] == "nurbolot":
#         print("Он есть")
#         break