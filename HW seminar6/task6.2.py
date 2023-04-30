# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

n=int(input("введите минимум диапазона "))
m=int(input("введите максимум диапазона "))
import random
some_list = [random.randint(1, 10) for i in range (10)]
print(some_list)
some_l=[]
for i in range (len(some_list)-1):
    if m>=some_list[i]>=n:
        some_l.append(i)
if m>=some_list[-1]>=n:
    some_l.append(10)
print(some_l)
