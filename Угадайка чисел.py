# # напишем программу, которая решает любое квадратное уравнение
# # квадратное уравнение вида: ax^2 + bx + c = 0
# import math
# a = int(input())
# b = int(input())
# c = int(input())
# x1 = 0
# x2 = 0
# D = b**2 - 4*a*c
# if a != 0:
#     if D > 0:
#         x1 = (-b + math.sqrt(D))/2*a
#         x2 = (-b - math.sqrt(D))/2*a
#         print("Уравнение имеет два корня:", x1, "и", x2)
#     elif D == 0:
#         x1 = -b/2*a
#         print("Уравнение имеет один корень:", x1)
#     else:
#         print("Уравнение не имеет корней")
# else:
#     print("Это не квадратное уравнение")
# #print(int(math.sqrt(a)))
from random import randint

print("Добро пожаловать в числовую угадайку!\n")


def is_valid(n, right_border):
    # n уже гарантированно число, просто проверяем диапазон
    return 1 <= n <= right_border


def play_round():
    # 1. Задаем границу
    while True:
        try:
            right = int(input("Введите правую границу диапазона: "))
            if right < 1:
                print("Граница должна быть больше 0!")
                continue
            break
        except ValueError:
            print("А может быть все-таки введем целое число?\n")

    x = randint(1, right)
    cnt = 0

    # 2. Игровой цикл угадывания
    while True:
        try:
            k = int(input(f"Введите число от 1 до {right}: "))
        except ValueError:
            print("А может быть все-таки введем целое число?")
            continue

        cnt += 1

        if is_valid(k, right):
            if k > x:
                print("Ваше число больше загаданного, попробуйте еще разок\n")
            elif k < x:
                print("Ваше число меньше загаданного, попробуйте еще разок\n")
            else:
                print("Вы угадали, поздравляем!")
                print(f"Всего попыток: {cnt}\n")
                break
        else:
            print(f"А может быть все-таки введем целое число от 1 до {right}?\n")


# Главный цикл всей программы
while True:
    play_round()

    # Логика перезапуска без дублирования кода
    ans = input("Хотите сыграть еще раз? (да/нет): ").lower().strip()
    while ans != "да" and ans != "нет":
        ans = input("Нужно ответить строго 'да' или 'нет': ").lower().strip()

    if ans == "нет":
        print("Спасибо за игру! Еще увидимся...")
        break