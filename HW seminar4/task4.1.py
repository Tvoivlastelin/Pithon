# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.Пользователь вводит 2 числа. n — кол-во элементов первого
# множества. m — кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.

n=int(input("введите кол-во элементов первого множества "))
m=int(input("введите кол-во элементов второго множества "))
some_list1 = []
for _ in range(n):
    number = int(input())
    some_list1.append(number)
some_list2 = []
for _ in range(m):
    number2 = int(input())
    some_list2.append(number2)
print(some_list1,some_list2)
print(set(some_list1+some_list2))