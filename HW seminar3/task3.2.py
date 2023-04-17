# Задача 18: Требуется найти в списке A[1..N]
# самый близкий по величине элемент к заданному
# числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в
# списке. В последующих  строках записаны N целых
# чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input())
some_list = []
for i in range (n):
    number = i+1
    some_list.append(number)
print(some_list)
x=int(input())
a=0
b=0
for j in some_list:
    if x>len(some_list):
        a=some_list[-1]
    elif x<j:
        b = some_list[0]
    elif x == j:
        print(x + 1)
        break
if a!=0:
    print(a)
if b!=0:
    print(b)
