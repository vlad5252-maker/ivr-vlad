"""x = 10780
while x != 0 or y != 0:
    if x == 0:
        print(y, "Это Y")
        break
    elif y == 0:
        print(x, "Это X")
        break
    if y > x:
        y = y % x
    else:
        x = x % y"""

n = int(input())
total = 0
while n != 0:
    if (n <= 10000) and 100 <= n <= 999 and n % 5 == 0 and n % 10 == 0:
        total += n
    n = int(input())
print(total)
