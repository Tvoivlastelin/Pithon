# Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
a = int(input('Введите трехзначное число '))
c = 0
if a < 100 or a > 999:
    print('это не трехзначное число')
while a > 0:
    c = c + a % 10
    a = a // 10
print(c)
