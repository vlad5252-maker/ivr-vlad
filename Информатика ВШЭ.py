# План подготовки к экзамену:
#     1) закончить курс "Поколение Python для начинающих"
#     2) пройти вложенные списки в курсе от поколения питон для продвинутых
# n = int(input())
# count = 0
# total = 0
# t = str(n)
# for i in range(len(t)):
#     if int(t[i]) % 2 == 0:
#         count += 1
#         total += int(t[i])
# if count == 0:
#     print(0)
# else:
#     print(total/count)
# print("hello world")
# n = [2,34,5,66,7,67]
# for i in range(len(n)):
#     print(n[i], end=' ')'''
# a = 'КОТ'
# for i in a:
#     for j in a:
#         for k in a:
#             for h in a:
#                 for r in a:
#                     s = i + j + k + h + r
#                     print(s)
# n = int(input())
# print(n // 60, n % 60)
# a = int(input())
# b = int(input())
# n = int(input())
# r = n * a + (n * b) // 100
# k = (n * b) % 100
# print(r, k)
# n = int(input())
# k = int(input())
# y = k % n
# print((n - y) % n)
# n = int(input())
# m = int(input())
# print((-m // n) * (-1))
# k1 = int(input())
# k2 = int(input())
# k3 = int(input())
# n1 = (-k1 // 2) * (-1)
# n2 = (-k2 // 2) * (-1)
# n3 = (-k3 // 2) * (-1)
# print(n1 + n2 + n3)
# k = int(input())
# n = int(input())
# print((n-1) // k + 1)
# n = int(input())
# m = int(input())
# x = n * m
# k = (x - 1) // 2 + 1
# print(k)
# h1 = int(input())
# m1 = int(input())
# h2 = int(input())
# m2 = int(input())
# if h1 < 10:
#     if m1 < 10:
#         print('0' + str(h1), ":", str(m1) + '0', sep='')
#     else:
#         print('0' + str(h1), ":", m1, sep='')
# elif m1 < 10:
#     print(h1, ":", '0' + str(m1), sep='')
# else:
#     print(h1, ":", m1, sep='')
# while h1 != h2:
#     if m1 == 59:
#         h1 += 1
#         m1 *= 0
#     else:
#         m1 += 1
#     if h1 < 10 and m1 < 10:
#         print('0' + str(h1), ":", '0' + str(m1), sep='')
#     elif h1 < 10:
#         print('0' + str(h1), ":", m1, sep='')
#     elif m1  10:
#         print(h1, ":", '0' + str(m1), sep='')
#     else:
#         print(h1, ":", m1, sep='')
# h1 = int(input())
# m1 = int(input())
# h2 = int(input())
# m2 = int(input())
#
# # Переводим стартовую и конечную точку в минуты от начала суток
# start_minutes = h1 * 60 + m1
# end_minutes = h2 * 60 + m2
#
# # Перебираем каждую минуту в этом диапазоне
# for total_minutes in range(start_minutes, end_minutes + 1):
#     # Получаем текущие часы и минуты
#     h = total_minutes // 60
#     m = total_minutes % 60
#
#     # Форматируем строку: :02d означает "вывести целое число шириной 2 знака, заполнив пустоту нулями"
#     print(f"{h:02d}:{m:02d}")
# n = int(input())
# while n > 100:
#     n //= 10
# k = n % 10
# print(k)
# n = int(input())
# s = ''
# while n != 0:
#     digit = n % 10
#     if digit != 0 and digit != 1:
#         s = str(digit) + s
#     n //= 10
# print(s)
# n = int(input())
# i = 0
#
# for k in str(n):
#     if int(k) % 2 == 0:
#         i += 1
#         print(str(i) + '-я четная цифра равна', k)
# if i == 0:
#     print("Четных цифр в числе нет")
# while n > 0:
#     last = n % 10
#     if last % 2 == 0:
#         i += 1
#         print(str(i) + '-я четная цифра равна', last)
#     n //= 10
# if i == 0:
#     print("Четных цифр в числе нет")
# num = int(input())                                # считываем число
# n = len(str(num))                                 # количество разрядов числа
# for i in range(1, n + 1):                         # проходим по всем разрядам числа от 1 до n
#      digit = num // 10 ** (n - i) % 10             # получаем i-ю цифру числа
#     ...                                           # обрабатываем i-ю цифру числа
# n = 3 * 144 + 2 * 12 + 4 * 1
# m = 2 * 9 + 7 * 1
# k = n % m
# s = ''
# print(k)
# while k > 0:
#     s = str(k % 6) + s
#     k //= 6
# print(s)
# n = int(input())
# m = int(input())
# flag = False
# for x in range(1, n):
#     for y in range(1, n):
#         for z in range(1, n):
#             if x + 3 * y + 2 * z == m:
#                 flag = True
#                 print(x, '+ 3*' + str(y), '+ 2*' + str(z), '=', m)
# if flag == False:
#     print("При заданных n и m решений не существует.")
# a = int(input())
# b = int(input())
# total = 0
# mx = -10*6
# mx_num = -1
# for i in range(a, b + 1):
#     for j in range(1, i+1):
#         if i % j == 0:
#           total += j
#     if total > mx:
#         mx = total
#         mx_num = i
#     total = 0
# print(mx_num, mx)
# a, b = int(input()), int(input())
#
# mx_num = -1
# mx_sum = -1
# for cur_num in range(a, b + 1):
#     cur_sum = 0
#     for j in range(1, cur_num + 1):
#         if cur_num % j == 0:
#             cur_sum += j
#     if cur_sum >= mx_sum:
#         mx_num = cur_num
#         mx_sum = cur_sum
# print(mx_num, mx_sum)
# k = int(input())
# l = int(input())
# m = int(input())
# n = int(input())
# if (k % 2 == 0 and l % 2 == 1) and (m % 2 == 0 and n % 2 == 1)or (k % 2 == 0 and l % 2 == 1) and (m % 2 == 1 and n % 2 == 0) or (k % 2 == 1 and l % 2 == 0) and (m % 2 == 1 and n % 2 == 0) or (k % 2 == 1 and l % 2 == 0) and (m % 2 == 0 and n % 2 == 1) :
#     print("YES")
# if (k % 2 == 0 and l % 2 == 0 and m % 2 == 0 and n % 2 == 0) or (k % 2 == 1 and l % 2 == 1 and m % 2 == 1 and n % 2 == 1):
#   print("YES")
# else:
#   print("NO")
# from math import *
# s = input()
# s_new = ''
# for i in range(ceil(len(s) / 2)):
#     s_new += s[i]
#     i_new = i
# for i in range(len(s)-1, i_new, -1):
#     s_new = s[i] + s_new
# print(s_new)
# n = int(input())
# l = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         l.append(i)
# print(l)
# n = int(input())
# l = []
# for i in range(n):
#     x = int(input())
#     l.append(x)
# for i in range(len(l) - 1):
#     total = l[i] + l[i + 1]
#     l[i] = total
# print(l)
# n = int(input())
# l = []
# new_l = []
# for i in range(n):
#     x = int(input())
#     l.append(x)
# for i in range(0, len(l), 2):
#     new_l.append(l[i])
# print(new_l)
# n = int(input())
# l = []
# for _ in range(n):
#     x = input()
#     l.extend(x)
# print(l)
# n = int(input())
# c = []
# q = ''
# for _ in range(n):
#     s = input()
#     c.append(s)
# k = int(input())
# for i in range(n):
#     if k > len(c[i]):
#         continue
#     else:
#         q += c[i][k-1]
# print(q)
# n = int(input())
# l = []
# for _ in range(n):
#     x = int(input())
#     l.append(x)
# for i in l:
#     if i < 0:
#         print(i)
# for i in l:
#     if i == 0:
#         print(i)
# for i in l:
#     if i > 0:
#         print(i)
# n = int(input())
# l = []
# for _ in range(n):
#     x = input()
#     if x not in l:
#         l.append(x)
# print(*l, sep='\n')
# n = int(input())
# l =[]
# for _ in range(n):
#     x = int(input())
#     l.append(x)
# print(*l, sep='\n')
# print()
# for i in l:
#     y = (i + 1) ** 2
#     print(y)
# n = int(input())
# l = []
# for _ in range(n):
#     x = int(input())
#     l.append(x)
# del l[l.index(max(l))]
# del l[l.index(min(l))]
# print(*l, sep='\n')
# n = int(input())
# strings = []
# for _ in range(n):
#     strings.append(input())
#
# search = input().lower()
#
# for string in strings:
#     if search in string.lower():
#         print(string)
# n = int(input())
# l_x = []
# l_y =[]
# for _ in range(n):
#     x = input()
#     l_x.append(x)
#
# k = int(input())
#
# for _ in range(k):
#     y = input()
#     l_y.append(y)
# for i in l_x:
#     for j in l_y:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)
# s = input().split()
# l = [i[0][0] for i in s]
# print('.'.join(l), end='.')
# s = input().split("\\")
# print('\\'.join(s))
# s = input().split('.')
# for i in s:
#     if int(i) <= 255:
#         flag = True
#     else:
#         flag = False
#         break
# if flag:
#     print("ДА")
# else:
#     print("НЕТ")
# n = input().split()
# print(n)
# n = input()
# n = int(n[1:])
# l1 = []
# l2 =[]
# for _ in range(n):
#     s = input()
#     l1.append(s)
# n = input().split()
# n = [int(i) for i in n]
# ind_mx = n.index(max(n))
# ind_mn = n.index(min(n))
#
# n[ind_mn], n[ind_mx] = n[ind_mx], n[ind_mn]
# print(n)
# n = input()
# n = int(n[1:])
# l = []
# for _ in range(n):
#     l.append(input())
# for i in l:
#     if "#" in i:
#         ind = i.index("#")
#         while "#" in i:
#             i = i[:ind].rstrip()
#         print(i)
#     else:
#         print(i.rstrip())
# print('\n'.join([i for i in input().split()]))
# print('\n'.join([str(i ** 2) for i in range(1, int(input()) + 1)]))
# print(' '.join([str(int(i) ** 3) for i in input().split()]))
# print(''.join([i for i in input() if i.isdigit()]))
# print(*[str(int(i) ** 2) for i in input().split() if int(i) % 2 == 0 and (int(i) ** 2) % 10 != 4 ])
# # Задача 1
# n = int(input())
# for i in str(n):
#     if int(i) % 2 != 1 and int(i) != 0:
#         continue
#     print(i, end='')
# # Задача 2
# s =
# for i in range(3, 31, 3):
#     s += i/(i + 2)
# print(round(s, 3))
# # Задача 3
# n = input().split()
# for i in range(len(n)):
#     for j in range(len(n) - 1):
#         if n[i][j] == n[i][j + 1]:
#             n.pop(i)
# print(' '.join(n))
# Задача 5
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# # реализация алгоритма сортировки выбором
# for i in range(n):
#     a[-1] = max(a)
#     a = a[:-1]
# print(a)
# l = input().split()
# m = input().split()
# l_m = []
# for i in range(len(l)):
#     l_m.append(int(l[i]) + int(m[i]))
# print(l_m)
# print([int(m[i]) + int(l[i]) for i in range(len(l))])
# print(max([len(i) for i in input().split()]))
# n = input().split()
# print([i[1:] + i[0] + "ки" for i in n])
# n = input().split("-")
# if len(n) == 4 and n[0].isdigit and len(n[0]) == 1 and n[1].isdigit and len(n[1]) == 3 and n[2].isdigit and len(n[2]) == 3 and n[3].isdigit and len(n[3]) == 4:
#     print("YES")
# else:
#     print("NO")
# Задача 1
# a, b = map(int, input().split())
# print((a + b) * 2, a * b)
# Задача 2
# n = input()
# print(int(n[-1] + n[1] + n[0]))
# Задача 3
# Задача 4
# k = input().split()
# if k[0] == k[2] or k[1] == k[3]:
#     print("YES")
# else:
#     print("NO")
# Задача 5
# n = int(input())
# mx = -1
# while n > 0:
#     last_digit = n % 10
#     mx = max(mx, last_digit)
#     n //= 10
# print(mx)
# Задача 6
# n = input().split()
# first = int(n[0])
# last = int(n[-1])
# l = [i for i in range(first, last + 1) if i % 2 == 0]
# l.sort(reverse=True)
# l = [str(i) for i in l]
# print(' '.join(l))
# Задача 7
# n = int(input())
# l = [int(input()) for i in range(n)]
# l_new = [str(i) for i in l if i % 10 == 3 and i % 7 == 0]
# print(len(l_new))
# Задача 8
# n = input().split()
# n = [int(i) for i in n]
# mx_ind = n.index(max(n))
# mn_ind = n.index(min(n))
# n[mx_ind], n[mn_ind] = n[mn_ind], n[mx_ind]
# print(*n)
# Задача 9
# n = input().split()
# n_int = [int(i) for i in n]
# c = sum(n_int)/len(n_int)
# n_new = [i for i in n_int if i > c]
# print(*n_new)
# Задача 10
# n = input().split()
# cnt = 0
# for i in range(len(n) - 1):
#     if n[i] == n[i + 1]:
#         cnt += 1
# print("YES" if cnt >= 1 else "NO")\
# Задача 11
# n = input()
# l = [int(i) for i in n if i.isdigit()]
# print(sum(l))
# Задача 12
# n = input().split()
# ln = [len(i) for i in n]
# print(max(ln))
# Задача 1
# n = input()
# l = [int(i) for i in n if int(i) % 2 == 0]
# if len(l) >= 2:
#     print(max(l) - min(l))
# else:
#     print(-1)
# Задача 2
# n = input().split()
# n = [int(i) for i in n]
# if abs(n[2] -  n[3]) == 3 or abs(n[2] -  n[3]) == 1:
#     print("YES")
# else:
#     print("NO")
# Задача 3
# n = input().split()
# cnt = 0
# int_n = [int(i) for i in n]
# for i in range(1, len(int_n) - 1):
#     if n[i] > n[i + 1] and n[i] > n[i - 1]:
#         cnt += 1
# print(cnt)
# Задача 4
# n = input().split()
# l = [i for i in range(len(n)) if ]
# Задача 5
# n = input()
# s = ''
# l = []
# # l = [i for i in n if i in {'a', 'e', 'i', 'o', 'u', 'y'}]
# i = 0
# while n[i] in {'a', 'e', 'i', 'o', 'u', 'y'}:
#     s += n[i]
#     i += 1
# l.append(s)
# print(l)
from functools import total_ordering
from glob import translate
from importlib.metadata import pass_none
from itertools import count

from unicodedata import category

# 1. Считываем матрицу 6х6
# A = []
# for _ in range(6):
#     row = list(map(int, input().split()))
#     A.append(row)
# print(A)
# #
# # 2. Переменные для хранения максимумов и их координат
# # Изначально ставим самое маленькое возможное число из условия (-10000)
# max_lower = -100000
# r_low, c_low = 0, 0
#
# max_upper = -100000
# r_upp, c_upp = 0, 0
#
# # 3. Полный обход матрицы
# for i in range(6):
#     for j in range(6):
#
#         # Если элемент в нижнем треугольнике (включая диагональ)
#         if i >= j:
#             if A[i][j] > max_lower:
#                 max_lower = A[i][j]
#                 r_low, c_low = i, j  # Запомнили строчку и столбец
#
#         # Если элемент в верхнем треугольнике
#         elif i < j:
#             if A[i][j] > max_upper:
#                 max_upper = A[i][j]
#                 r_upp, c_upp = i, j  # Запомнили строчку и столбец
#
# # 4. Меняем их местами (наш олимпиадный трюк)
# A[r_low][c_low], A[r_upp][c_upp] = A[r_upp][c_upp], A[r_low][c_low]
#
# # 5. Красиво выводим измененную матрицу построчно
# for row in A:
#     print(*row)
# n = map(int, input().split())
# print(n)
# A = []
# for i in range(6):
#     row = list(map(int, input().split()))
#     A.append(row)
# total = sum(A[0])
# print(total)
# Если на входе строго два числа (например, стороны прямоугольника)
# a, b = map(int, input().split())
# print(a, b)
# A = []
# prod = 1
# for i in range(6):
#     row = list(map(int, input().split()))
#     A.append(row)
# for i in range(6):
#     for j in range(6):
#         if i + j == len(A) - 1:
#             prod *= A[i][j]
# print(prod)
# A = []
# for i in range(6):
#     row = list(map(int, input().split()))
#     A.append(row)
# mx = A[0][0]
# mx_i = 0
# mx_j = 0
# for i in range(6):
#     for j in range(6):
#         if A[i][j] > mx:
#             mx = A[i][j]
#             mx_i = i
#             mx_j = j
# print(mx, mx_i + 1, mx_j + 1)
# n = list(map(int, input().split()))
# print("YES" if abs(n[0] - n[2]) == abs(n[1] - n[3]) else "NO")
# n = list(map(int, input()))
# cnt = 0
# mx_cnt = 0
# for i in n:
#     if i == 7:
#         cnt += 1
#         mx_cnt = max(mx_cnt,  cnt)
#     else:
#         cnt = 0
# print(mx_cnt)
# Задача 1
# s = 0
# for i in range(1, 20, 2):
#     s += i/(i + 1)
# print(f'{s: .4f}')
# Задача 2
# n = list(map(int, input().split()))
# if max(abs(n[0] - n[2]), abs(n[1] - n[3])) == 1:
#     print("YES")
# else:
#     print("NO")
# Задача 3
# n = list(map(int, input().split()))
# l = list(map(int, set(n)))
# print(*l)
# Задача 4
# A = []
# for _ in range(6):
#     row = list(map(int, input().split()))
#     A.append(row)
# mn = A[0][0]
# for i in range(6):
#     for j in range(6):
#         if i == j:
#             if A[i][j] < mn:
#                 mn = A[i][j]
# print(mn)
# Задача 5
# s = input()
# l = 0
# mx_l = 0
# for i in s:
#     if i == ' ':
#         l += 1
#         mx_l = max(mx_l, l)
#     else:
#         l *= 0
# print(mx_l)
# n = int(input())
# for i in range(n):
#     s = input()
# l = 0
# mx_l = 0
# for i in range(len(s) - 1):
#     if s[i+1] >= s[i]:
#         l += 1
#         mx_l = max(mx_l, l)
#     else:
#         l = 0
# print(mx_l)
# Задача 1
# s = 0
# for i in range(2, 23, 2):
#     s += i/(i+1)
# print(f'{s: .3f}')
# Задача 2
# n = list(map(int, input().split()))
# if abs(n[0] - n[2]) == abs(n[1] - n[3]) or (n[0] == n[2] or n[1] == n[3]):
#     print("YES")
# else:
#     print("NO")
# Задача 3
# n = list(map(int, input().split()))
# l = [i for i in n if n.count(i) == 1]
# print("YES" if len(l) == len(n) else "NO")
# Задача 4
# A = []
# for i in range(6):
#     row = list(map(int, input().split()))
#     A.append(row)
# total = 0
# for i in range(6):
#     for j in range(6):
#         if i + j == 5:
#             total += A[i][j]
# print(total)
# Задача 5
# s = input()
# mx = 0
# l = 0
# for i in range(len(s)):
#     if s[i] == "x":
#         l += 1
#         mx = max(mx, l)
#     else:
#         l = 0
# print(mx)
# l = list(map(int, input().split()))
# print(*list(map(int, set(l))))
# Задача 1
# s = input()
# cnt = 0
# for i in s[::-1]:
#     if i == "!":
#         cnt += 1
#     else:
#         break
# print(cnt)
# Задача 2
# n = list(map(int, input().split()))
# total = 0
# l = []
# for i in range(1, len(n) - 1):
#     # total = n[i] + n[i + 1]
#     l.append(n[i] + n[i + 1])
# n[1:-1] = l
# print(n)
# Задача 3
# n = list(map(int, input().split()))
# for i in n:
#     if n.count(i) >= 3:
#         print("DANGER")
#         break
# else:
#     print("ОК")
# Задача 4
# A = []
# for _ in range(6):
#     row = list(map(int, input().split()))
#     A.append(row)
# cnt = 0
# for i in range(1, 5):
#     if A[i][0] == 1:
#         if A[i][-1] == 1:
#             cnt += 2
#         else:
#             cnt += 1
#     elif A[i][-1] == 1:
#         cnt += 1
# for i in A[0]:
#     if i == 1:
#         cnt += 1
# for i in A[-1]:
#     if i == 1:
#         cnt += 1
# print(cnt)
# Задача 5
# s = input()
# mn = 10 ** 6
# l = 0
# flag = False
# for i in range(len(s)):
#     if s[i] == ".":
#         l += 1
#         flag = True
#         mn = min(mn, l)
#     else:
#         l = 0
# print(mn if flag else 0)
# k = int(input())
# h = k // (60*60)
# m = k // (24*60)
# s = k % 60
# if h >= 24:
#     if m >= 60:
#         print(f'0{abs(24 - h)}:0{abs(60 - m)}:0{s}')
#     else:
#         print(f'0{abs(24 - h)}:0{m}:0{s}')
# elif h < 24:
#     if m >= 60:
#         print(f'0{h}:0{abs(60 - m)}:0{s}')
#     else:
#         print(f'0{h}:0{m}:0{s}')
# Задача 2
# n = list(input())
# cnt = 0
# for i in range(int(n[0]), int(n[1]) + 1):
#     for j in range(2, 10):
#         if i % j != 0 and str(i)[::-1] % 3 == 0:
#             cnt += 1
# print(cnt)
# Задача 3
# n = int(input())
# cnt_zero = 0
# l = list(map(int, input().split()))
# while 0 in l:
#     l.remove(0)
#     cnt_zero += 1
# for _ in range(cnt_zero):
#     l.append(-1)
# print(*l)
# Задача 4
# n = int(input())
# s = ''
# A = []
# for i in range(n):
#     row = input().split()
#     A.append(row)
# for i in range(len(A)):
#     for j in range(len(A)):
#         if j > i:
#             s += A[i][j]
# if s == s[::-1]:
#     print("PALINDROME")
# else:
#     print(s)
# Итог: обосался на экзамене и зачем-то завершил испытание не отправив математику
#       (но все равно поступил! ХАХАХААХ!)
# n = list(map(int, input().split()))
# mx = max(n)
# while mx in n:
#     n.remove(mx)
# print(max(n))
# n = list(map(int, input().split()))
#
# max1 = float('-inf')
# max2 = float('-inf')
#
# for x in n:
#     if x > max1:
#         max2 = max1  # Бывший первый становится вторым
#         max1 = x     # Появляется новый первый
#     elif x > max2 and x != max1:
#         max2 = x     # Обновляем второго, если он не равен первому
#
# print(max2)
# s = input()
# letters = 0
# digits = 0
# for i in s:
#     if i.isalpha():
#         letters += 1
#     elif i.isdigit():
#         digits += 1
# if letters > digits:
#     print("LETTERS")
# elif letters < digits:
#     print("DIGITS")
# else:
#     print("EQUAL")
# n = input().split()
# n.insert(0, n[-1])
# n.pop()
# print(*n)
# s = input()
# s_lst = s.split(" - ")
# try:
#     first = s.index("-")
#     second = s.rindex("-")
#     print(s[:first - 1])
#     print(s[first + 2: second - 1])
#     print(s[second + 2:])
# except:
#      print("Ошибка: строка не соответствует формату Название - Исполнитель - Год")
# if s.count("-") == 2:
#     for i in s_lst:
#         print(i)
# else:
#     print("Ошибка: строка не соответствует формату Название - Исполнитель - Год")
# s = input()
# s = s.lower()
# s = s.strip()
# s = s.strip("руб")
# s = float(s)
# print(s)
# print(float(input().lower().strip(" руб")))
# n = int(input())
# s = []
# for _ in range(n):
#     s.append(input())
# i = 0
# prefix = ''
# while s[0][i] == s[1][i]:
#     prefix += s[0][i]
#     i += 1
# for j in s:
#     print(j.removeprefix(prefix))
# n = list(map(float, input().split()[1:]))
# for i in range(len(n)):
#     n[i] += 5
# print(f"Смещение: X={n[0]}, Y={n[1]}, Z={n[2]}")
# s = list(map(chr, map(int, input().split())))
# print(s)
# print(*list(map(chr, map(int, input().split()))), sep='')
# print("Он ударил в медный таз"
#       " И вскричал: «Кара-барас!»")
# put your python code here
# ip = input().split(".")
# for i in range(len(ip)):
#     try:
#         if len(ip) == 4 and 0 <= int(ip[i]) <= 255:
#             ip[i] = str(bin(int(ip[i])))[2:].zfill(8)
#         else:
#             print("Некорректный IP-адрес")
#             break
#     except:
#         print("Некорректный IP-адрес")
#         break
# else:
#     print(".".join(ip))
# print("a\tb".expandtabs())
# print("ab\tb".expandtabs(4))
# print("abcd\te".expandtabs(4))
# print("a\tb\tc".expandtabs(6))
# s = input()
# cnt = ''
# for i in s:
#     cnt += str(s.count(i))
# trans = str.maketrans(s, cnt)
# print(s.translate(trans))
# s = input().lower().replace(" ", "").split(";")
# # print(s[0], s[1])
# if len(s[0]) >= len(s[1]):
#     for i in range(len(s[0])):
#         if s[0].count(s[0][i]) >= s[1].count(s[0][i]):
#             flag = True
#             # print(flag)
#         else:
#             flag = False
#             print(flag)
#             break
#     else:
#         print(flag)
# else:
#     print(False)
# def cnt_up_and_lower(s):
#     cnt_up, cnt_lw = 0, 0
#     a = [cnt_up += 1 for i in s if i.isupper() elif i.islower() cnt_lw += 1]
# # объявление функции
# def draw_triangle(fill, base):
#     print(*[fill * i for i in range(1, base // 2 + 2)], sep='\n')
#     print(*[fill * i for i in range(base // 2, 0, -1)], sep='\n')
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)
# def print_symbol_counts(s):
#     # Приводим к нижнему регистру и сортируем уникальные буквы
#     unique_letters = sorted(set(s))
#     for letter in unique_letters:
#         count = s.count(letter)
#         print(f"{letter}: {count}")
#
# # Считываем данные
# s = input().lower()
#
# # Вызываем функцию
# print_symbol_counts(s)
# total = sum(list(map(int, list(input()))))
# print(total)
# объявление функции
# def math_round_to_int(num):
#     pass
#
# # считываем данные
# num = float(input())
#
# # вызываем функцию
# print(math_round_to_int(num))
# print(round(float(input())))
# print("000000045".lstrip("0"))
# print("0000000".lstrip("0"))
# def math_round_to_int(num):
#     l = str(num).split(".")
#     if l[1][0] != "5":
#         return round(num)
#     elif len(l[1][1:].lstrip("0")) > 0:
#         return round(num)
#     else:
#         return int(l[0]) + 1
# n = float(input())
# print(math_round_to_int(n))
# from math import ceil, floor
# def math_round_to_int(num):
#     if num - int(num) >= 0.5:
#         return ceil(num)
#     else:
#         return floor(num)
# n = float(input())
# print(math_round_to_int(n))
# def get_factors(num):
#     l = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             l.append(i)
#     return l
# n = int(input())
# print(get_factors(n))
# объявление функции
# объявление функции
# def get_last_index(data, value):
#     try:
#         return len(data) - 1 - data[::-1].index(value)
#     except:
#         return "ERROR!"
# # считываем данные
# data = eval(input())
# value = eval(input())
#
# # вызываем функцию
# print(get_last_index(data, value))
# put your python code here
# l = []
# k = int(input())
# for i in range(k):
#     n = list(map(int, input().split()))
#     l += n
# l.sort()
# print(*l)
# объявление функции
# def is_palindrome(text):
#     l = []
#     for i in text:
#         if i.isalpha():
#             l.append(i)
#     return l == l[::-1]
# # считываем данные
# txt = input().lower()
#
# # вызываем функцию
# print(is_palindrome(txt))
# объявление функции
# def is_one_away(word1, word2):
#     cnt = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 cnt += 1
#         return cnt == 1
#     else:
#         return False
#
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))
# объявление функции
# def convert_to_python_case(text):
#     res = text[0].lower()
#     l = []
#     for i in text[1:]:
#         if i.isupper():
#             l.append(res)
#             res = i.lower()
#         else:
#             res += i
#     l.append(res)
#     return "_".join(l)
# txt = input()
# print(convert_to_python_case(txt))
# объявление функции
# def is_prime(num):
#     if num < 2:
#         return False
#     cnt = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             cnt += 1
#     return cnt == 2
#
#
# # Объявление функции
# def get_next_prime(num):
#     next_num = num + 1  # Начинаем искать строго со следующего числа
#
#     # Будем увеличивать число, пока не найдем простое
#     while not is_prime(next_num):
#         next_num += 1
#
#     return next_num
#
#
# # Считываем данные
# n = int(input())
#
# # Вызываем функцию
# print(get_next_prime(n))
# cnt = 0
# while not False:
#     cnt += 1
#     if cnt == 3:
#         break
# print(cnt)
# объявление функции
# def is_password_good(password):
#     cnt_up = 0
#     cnt_low = 0
#     cnt_dig = 0
#     if len(password) >= 8:
#         for i in password:
#             if not i.isdigit() and i.isupper():
#                 cnt_up += 1
#             elif not i.isdigit() and i.islower():
#                 cnt_low += 1
#             elif i.isdigit():
#                 cnt_dig += 1
#         return cnt_up >= 1 and cnt_low >= 1 and cnt_dig >= 1
#     else:
#         return False
#
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))
# text = "((()))"
# while "()" in text:
#     text = text.replace("()", "")
# print(text, text == '')
# объявление функции
# def is_correct_bracket(text):
#     while "()" in text:
#         text = text.replace("()", "")
#     return text == ''
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))
# объявление функции
# def is_prime(n):
#     if n == 1:
#         return False
#     cnt = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             cnt += 1
#     return cnt == 2
# def is_2(num):
#     return num % 2 == 0
#
# def is_valid_password(password):
#     return password[0] == password[0][::-1] and is_prime(int(password[1])) and is_2(int(password[2])) and len(password) == 3
#
# # считываем данные
# psw = input().split(":")
#
# # вызываем функцию
# print(is_valid_password(psw))
# def get_circle(radius):
#     from math import pi
#     return 2 * pi * radius, pi * radius ** 2
# R = int(input())
# C, S =  get_circle(R)
# print(C, S)
# def solve(a, b, c):
#     D = b ** 2 - 4 * a * c
#     if D >= 0:
#         return (-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)
# d, e, f = int(input()), int(input()), int(input())
# print(*solve(d, e, f))
# объявление функции
# def draw_triangle(l, h):
#     for i in range(1, l + 1, 2):
#         print(("*" * i).center(l).rstrip())
#
# draw_triangle(15, 8)
#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************
# объявление функции
# def number_to_words(num):
#     s1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     s2 = ['один', 'две', 'три', 'четыр', 'пят', 'шест', 'сем', 'восем', 'девят']
#     s3 = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#
#     if 1 <= num <= 9:
#         return s1[num - 1]
#     elif 11 <= num <= 19:
#         return s2[num - 11] + "надцать"
#     elif num % 10 == 0:  # Числа 10, 20, 30... проверяем через остаток
#         return s3[(num // 10) - 1]
#     else:  # Для чисел типа 25, 85, 43
#         desyatki = s3[(num // 10) - 1]
#         edinicy = s1[(num % 10) - 1]  # Просто берем остаток от деления
#         return desyatki + " " + edinicy
#
#
# # Считываем данные
# n = int(input())
# print(number_to_words(n))
# объявление функции
# def get_month(language, number):
#     r =  ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     e =  ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if language == "ru":
#         return r[number - 1]
#     elif language == "en":
#         return e[number - 1]
# # считываем данные
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))
# объявление функции
# def is_magic(date):
#     date_l = list(map(int, date.split(".")))
#     return date_l[0] * date_l[1] == str(date_l[2])[-2:]
#
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))
# объявление функции
# def is_pangram(text):
#     text = "".join(text.split()).lower()
#     return len(set(text)) == 26  # Возвращает True, если длина 26, иначе False

# def is_pangram(text):
#     text = "".join(text.split()).lower()
#     if len(sorted(set(text))) == 26:
#         return True
#     else:
#         return False
# считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))
# m, h = float(input()), float(input())
# x = m / h ** 2
# if 18.5 <= x <= 25:
#     print("Оптимальная масса")
# elif x < 18.5:
#     print("Недостаточная масса")
# elif x > 25:
#     print("Избыточная масса")
# m, h = float(input()), float(input())
# imt = m / h ** 2
# category = ( "Недостаточная масса" if imt < 18.5 else "Оптимальная масса" if imt <= 25 else "Избыточная масса" )
# s = input()
# ru = (len(s) * 60) // 100
# kop = (len(s) * 60) % 100
# print(f"{ru} р. {kop} коп.")
# x = (int(input()) - 2000) % 12
# animals = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
# print(animals[x])
# n = input()
# res = []
# while len(n) > 0:
#     res.append(n[-3:])
#     n = n[:-3]
# res.reverse()
# print(",".join(res))
# n = int(input())
# one, two, three, four = 0, 0, 0, 0
# for _ in range(n):
#     x, y = map(int, input().split())
#     if x > 0 and y > 0:
#         one += 1
#     elif x < 0 and y > 0:
#         two += 1
#     elif x < 0 and y < 0:
#         three += 1
#     elif x > 0 and y < 0:
#         four += 1
# print(f"Первая четверть: {one}", f"Вторая четверть: {two}", f"Третья четверть: {three}", f"Четвертая четверть: {four}", sep='\n')
# l = list(map(int, input().split()))
# cnt = 0
# for i in range(len(l) - 1):
#     if l[i] < l[i + 1]:
#         cnt += 1
# print(cnt)
# l = input().split()
# res = []
# for i in range(0, len(l) - 1, 2):
#     res.append(l[i + 1])
#     res.append(l[i])
# print(" ".join(res) if len(res) == len(l) else " ".join(res + list(l[-1])))
# n = input().split()
# n.insert(0, n[-1])
# n.pop()
# print(*n)
# n = list(set(input().split()))
# print(len(n))
# n = input().split()
# res = []
# for i in n:
#     if i  not in res:
#         res.append(i)
# print(len(res))
# k = int(input())
# l = []
# flag = False
# for _ in range(k):
#     l.append(int(input()))
# prod = int(input())
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[j] * l[i] == prod:
#             flag = True
#             break
# if flag:
#     print("ДА")
# else:
#     print("НЕТ")
# T, R = input(), input()
# if T == R:
#     print("ничья")
# elif T == "камень" and R == "бумага" or T == "бумага" and R == "ножницы" or T == "ножницы" and R == "камень":
#     print("Руслан")
# else:
#     print("Тимур")
# T, R = input(), input()
# if T == R:
#     print("ничья")
# elif T == "камень" and R == "бумага" or T == "бумага" and R == "ножницы" or T == "ножницы" and R == "камень" or T == "ящерица" and R == "камень" or T == "камень" and R == "Спок" or T == "ножницы" and R == "Спок" or T == "Спок" and R == "ящерица":
#     print("Руслан")
# else:
#     print("Тимур")
# text = input()
# mx, cnt = 0, 0
# for i in text:
#     if i != "О":
#         cnt += 1
#         mx = max(cnt, mx)
#     else:
#         cnt = 0
# print(mx)
# print(max(list(map(len, input().split("О")))))
# n = int(input())
# res = []
# for i in range(1, n + 1):
#     f = input()
#     try:
#         ind_a = f.index("a")
#         f = f[ind_a:]
#         ind_n1 = f.index("n")
#         f = f[ind_n1:]
#         ind_t = f.index("t")
#         f = f[ind_t:]
#         ind_o = f.index("o")
#         f = f[ind_o:]
#         ind_n2 = f.index("n")
#         f = f[ind_n2:]
#         res.append(i)
#     except ValueError:
#         continue
# print(*res)
# n = int(input())
# res = []
# for i in range(1, n + 1):
#     f = input()
#     target = "anton"
#     ind = 0
#     for char in f:
#         if char == target[ind]:
#             ind += 1
#             if ind == 5:
#                 res.append(i)
#                 break
# print(*res)
# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     print(num % 2, end=' ')
#     res += (num % 2 == 1) and (num > 1)
# print()
# print(res)
# list1 = [1, 2, 3]
# list1_new = list1.copy()
# print(list1_new)
# n = int(input())
# for i in range(1, n + 1):
#     print(list(range(1, i + 1)))
# n = int(input())
# print(n)
# k, p, s = int(input()), int(input()), int(input())
# k_firs_septm = k * (p / 100)
# print(k_firs_septm)

# n = int(input())
# m = set()
# for _ in range(n):
#     s = input().split()
#     if s[0] == 'ADD':
#         m.add(s[1])
#     elif s[0] == 'PRESENT':
#         print("YES" if s[1] in m else "NO")
#     elif s[0] == 'COUNT':
#         print(len(m))

# n = int(input())
# dct = {}
# for _ in range(n):
#     x, y, n = input().split()
#     if x in dct:
#         if y == "OUT":
#             dct[x] -= int(n)
#         else:
#             dct[x] += int(n)
#     else:
#         if y == "OUT":
#             dct[x] = -int(n)
#         else:
#             dct[x] = int(n)
# print(dict([i for i in sorted(dct.items())]))

# n = int(input())
# dct = {}
# for _ in range(n):
#     product, price, count = input().split()
#     if product in dct:
#         dct[product] += int(price) * int(count)
#     else:
#         dct[product] = int(price) * int(count)
# print(dict( [i for i in sorted(dct.items())]))

# n = int(input())
# dct = {}
# for _ in range(n):
#     data, total = input().split()
#     data = data[:7]
#     if data not in dct:
#         dct[data] = int(total)
#     else:
#         dct[data] += int(total)
# print(dct)

# n = int(input())
# dct = {}
# for _ in range(n):
#     product, price = input().split()
#     if product in dct:
#         dct[product].append(int(price))
#     else:
#         dct[product] = [int(price)]
# for i in dct:
#     dct[i] = sum(dct[i]) // len(dct[i])
# print(dict([i for i in sorted(dct.items())]))

# 5
# Tea 100
# Tea 110
# Coffee 150
# Coffee 150
# Sugar 52

# n = int(input())
# dct = {}
# for _ in range(n):
#     category, k  = input().split()
#     k = int(k)
#     s = input().split()[:k]
#     for i in s:
#         dct[i] = category
# print(dct)

# n = int(input())
# dct = {}
#
# for _ in range(n):
#     client, amount = input().split()
#     if client in dct:
#         dct[client][1] += int(amount)
#         dct[client][0] += 1
#     else:
#         dct[client] = [1, int(amount)]
# print(dct)

# n = int(input())
# used = set()
#
# for _ in range(n):
#     surname, name = input().split()
#
#     if surname not in used:
#         login = surname
#     else:
#         login = f"{surname}_{name}"
#         if login in used:
#             cnt = 1
#             login = f"{surname}_{name}_{cnt}"
#
#             while login in used:
#                 cnt += 1
#                 login = f"{surname}_{name}_{cnt}"
#     print(login)
#     used.add(login)


# n = int(input())
# dct = {}
#
# while True:
#     num = input()
#     if "".join(num.split()).isdigit():
#         num = set(map(int, num.split()))
#     else:
#         break
#     s = input()
#     if s == "YES" or s == "NO":
#         if len(dct) == 0:
#             dct[s] = num
#         else:
#             dct[s].add(num)
# res = dct['YES'] - dct['NO']
# print(*(i for i in res))


# def dictionary_sorter(data_dict):
#     data_dict = {value: key for key, value in data_dict.items()}
#     lst = sorted(data_dict.items())
#     dct = {value: key for key, value in dict(lst).items()}
#     return dct

# def digit_sum(n):
#     if len(str(n)) == 1:
#         return n
#     return n % 10 + digit_sum(n // 10)

# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
#
#
# nums = list(map(int, input().split()))
# total = sum([i for i in nums if i % 2 == 0])
# count_unique = len(set(nums))
# s = input()
# while "()" in s:
#     s = s.replace("()", "")
# if len(s) == 0:
#     print("Yes")
# else:
#     print("No")


# def analyze_text(text):
#     table = str.maketrans('.,!?:;"()', "         ")
#     text = text.translate(table).lower()
#     unique_count = len(set(text.split()))
#     repeated_words = sorted([i for i in set(text.split()) if text.split().count(i) > 1])
#     palindromes = sorted([i for i in set(text.split()) if i == i[::-1]])
#     dct = {
#         'unique_count': unique_count,
#         'repeated_words': repeated_words,
#         'palindromes': palindromes
#     }
#     return dct

# t = "Wow! Did Hannah see that Race car? Mom was there too. Hannah did see it!"
#
# print(analyze_text(t))


# lst = list(int(input()) for _ in range(3))
# if len(list(filter(lambda n: n % 2 == 0, lst))) >= 1 and len(list(filter(lambda n: n % 2 == 1, lst))) >= 1:
#     print("OK")
# class Veсtor:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"({self.x}, {self.y})"

# import sys
# def printer(*args, sep=' ', end='\n', **kwargs):
#     print(*args, sep=sep, end=end)
#     print(*kwargs.items(), sep=sep, end=end)
# exec(sys.stdin.read())


# def foo(**kwargs):
#     print(kwargs)
# foo(a=1, b=2, c=3)

# grades_history = [
#     ('Анна', 5),
#     ('Игорь', 4),
#     ('Анна', 4),
#     ('Ольга', 5),
#     ('Игорь', 5)
# ]
# dct = {}
# for key, value in grades_history :
#     if key in dct:
#         dct[key].append(value)
#     else:
#         dct[key] = [value]
# print(dct)

# visitors = [101, 102, 101, 105, 102, 110, 105]
# print(list(set(visitors)))


    # ivan_friends = {'Алексей', 'Мария', 'Олег', 'Диана'}
    # anna_friends = {'Мария', 'Петр', 'Диана', 'Всеволод'}
    # print(ivan_friends - anna_friends)

# text = "Питон это круто и это факт Питон рулит"
#
# # Разбиваем строку на список слов в нижнем регистре
# words = text.lower().split()
# # Сейчас words равен: ['питон', 'это', 'круто', 'и', 'это', 'факт', 'питон', 'рулит']
#
# word_counts = {}
#
# for word in words:
#     word_counts[word] =  word_counts.get(word, 0) + 1
# print(word_counts)

# n = int(input())
# possible = set(range(1, n + 1))
#
# while True:
#     line = input()
#     if line == 'HELP':
#         break
#
#     current_set = set(map(int, line.split()))
#     answer = input()
#     if answer == 'YES':
#          possible &= current_set
#     else:
#         possible -= current_set
#
#
# print(*(sorted(possible)))

# nums = list(map(int, input().split()))
# st = set()
# for i in nums:
#     if i not in st:
#         st.add(i)
#         print('NO')
#     else:
#         print('YES')


# n, m = map(int, input().split())
# anns_nums, boris_nums = set(), set()
# for _ in range(n):
#     num = int(input())
#     anns_nums.add(num)
# for _ in range(m):
#     num = int(input())
#     boris_nums.add(num)
# answer_1 = set.intersection(anns_nums, boris_nums)
# answer_2 = set.difference(anns_nums, boris_nums)
# answer_3 = set.difference(boris_nums, anns_nums)
#
# print(len(answer_1), *answer_1, sep='\n')
# print(len(answer_2), *answer_2, sep='\n')
# print(len(answer_3), *answer_3, sep='\n')

# n = int(input())
# lst = []
# for _ in range(n):
#     langs = set()
#     for _ in range(int(input())):
#         lang = input()
#         langs.add(lang)
#     lst.append(langs)
#
# answer1 = set.intersection(*lst)
# answer2 = set.union(*lst)
# print(len(answer1), *answer1, sep='\n')
# print(len(answer2), *answer2, sep='\n')
# import sys
# words = sys.stdin.read().split()
# dct = {}
#
# for i in words:
#     dct[i] = dct.get(i, 0) + 1
#
# max_count = max(dct.values())
#
# res = [word for word, count in dct.items() if count == max_count]
#
# print(min(res))

# n = int(input())
# dct1 = {}
# for _ in range(n):
#     key, word = input().split()
#     dct1[key] = word
#     dct1[word] = key
#
# s = input()
#
# print(dct1[s])

# import sys
# words = sys.stdin.read().splitlines()
#
# dct = {}
#
# for i in words:
#     dct[i] = dct.get(i, 0) + 1
# dct = dict(sorted(dct.items()))
#
# for name, count in dct.items():
#     print(name, count)

# s = input()
# cnt = 0
# for i in range(len(s)):
#     cnt = 1
#     last = s[i]
#     while s[i] == last:
#         i += 1
#         cnt += 1
#     if cnt != 1:
#         print(f"{s[i]}{cnt}")

# nums = list(map(int, input().split()))
# ind_mx, ind_mn = nums.index(max(nums)), nums.index(min(nums))
# nums[ind_mx], nums[ind_mn] = nums[ind_mn], nums[ind_mx]
# print(nums)


# nums = list(map(int, input().split()))
# ind_mn, ind_mx = 0, 0
# for i in range(1, len(nums)):
#     if nums[i] > nums[ind_mx]:
#         ind_mx = i
#     if nums[i] < nums[ind_mn]:
#         ind_mn = i
#
# nums[ind_mn], nums[ind_mx] = nums[ind_mx], nums[ind_mn]
#
# print(*nums)



# Задача 3. Большой сдвиг
#
# Условие: Дан список чисел. Циклически сдвиньте элементы списка вправо (последний элемент становится первым, первый — вторым и так далее) K раз.
# Подвох: Сделать это нужно эффективно, так как список может быть большим, а K — очень большим (больше длины самого списка).
# Формат ввода:
# В первой строке вводится список чисел через пробел. Во второй строке — целое число K (количество сдвигов, K ≥ 0).
# Формат вывода:
# Сдвинутый список чисел через пробел.
# • Пример ввода:text
# 1 2 3 4 5
# 2
# Используйте код с осторожностью.
# • Пример вывода: 4 5 1 2 3

# nums = list(map(int, input().split()))
#
# k = int(input())
#
# n = k % len(nums)
#
# print(*(nums[-n:] + nums[:-n]))

# n = int(input())
#
# s = list(map(int, input().split()))
# l = []
# for i in s:
#     if i not in l:
#         l.append(i)
#
# print(len(l), 1, len(l))
# print(l)



# n, s = map(int, input().split())
# nums = list(map(int, input().split()))
# cnt = 0
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == s:
#             cnt += 1
# print(cnt)

# n = int(input())
#
# if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
#     print('YES')
# else:
#     print('NO')
#
# k, m, n = int(input()), int(input()), int(input())
#
# v = k / (2 * m)
#
# res = n / v
# if res - int(res) > 0:
#     print(res + (1 - (res - int(res))))
#
# print(int(res))

# w = int(input())
# flag = False
# for i in range(2, w, 2):
#     if (w - i) % 2 == 0:
#         flag = True
#         break
# if flag:
#     print('YES')
# else:
#     print('NO')


# s = '1' * 9 + '2' * 22
#
# while '111' in s or '222' in s:
#     while '111' in s:
#         s = s.replace('111', '2', 1)
#
#     while '222' in s:
#         s = s.replace('222', '1', 1)
# print(s)


# start = int(input())
# stop = int(input())
# flag = True
# n = input()
# while n:
#     if not(start <= int(n) <= stop):
#         flag = False
#     n = input()
# print(flag)

# word = input()
#
# print(('a' in word or 'o' in word) and ('e' not in word and 'i' not in word))

print(round(2.5))