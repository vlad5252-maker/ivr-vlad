"""k = int(input())
n = int(input())
print(n%k)
"""
# задание C
"""v = int(input())
t = int(input())
s = 0 + v*t
y = s % 54
print(y)"""
# задание D
"""n = int(input())
print(n%10)"""
# задание E
"""
n = int(input())
print(n // 10)"""
# задание F
"""
n = int(input())
print((n // 10) % 10)"""
# задание G
"""n = int(input())
# Количество минут в сутках
minutes_in_day = 24 * 60

# Берём остаток от деления на минуты в сутках,
# чтобы учесть, что n может быть больше суток
n = n % minutes_in_day

# Находим часы и минуты
hours = n // 60
minutes = n % 60

print(hours, minutes)"""
# задание H
"""
a = int(input())
b = int(input())
n = int(input())
r = n * a + (n * b) // 100
k = (n * b) % 100
print(r, k)"""
# I
"""
n = int(input())
firs = n // 100
second = (n // 10) % 10
third = n % 10
suma = firs + second + third
print(suma)"""
# J
"""
n = int(input())
a = n // 100000
b = (n // 10000) % 10
c = (n // 1000) % 10
d = (n // 100) % 10
e = (n % 100) // 10
f = n % 10
suma = a + b + c + d + e + f
print(suma)"""
# M
# h = int(input())
# a = int(input())
# b = int(input())
# print((h - b - 1) // (a - b) + 1)
# k, p, s = int(input()), int(input()), int(input())
# k_firs_septm = k * (p / 100)
# print(k_firs_septm)
n, m = map(int, input().split())
dct = {}
for _ in range(n):
    key, value = input().split()
    if key in dct:
        dct[key].append(value)
    else:
        dct[key] = [value]
cnt = 0
lst = []
for _ in range(m):
    value = input()
    for i in dct:
        if value not in dct[i]:
            cnt += 1
    lst.append(cnt)
    cnt = 0
print(*lst, sep='\n')