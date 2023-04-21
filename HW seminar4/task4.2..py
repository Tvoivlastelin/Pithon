#  В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
#  причём кусты высажены только по окружности. Таким образом, у каждого куста есть
#  ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
#  различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта
#  система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий
#  модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды
#  с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за
#  один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# list_test = [1, 2, 3, 4, 5, 7, 8, 9]
# k = int(input("Введите число сдвига"))
# value = list_test[k:]
# for i in list_test[:k]:
#     value.append(i)
# print(value)

n=int(input("введите кол-во кустов черники "))
import random
some_list = [random.randint(1, n) for i in range (n)]
print(some_list)
k=3
max=sum(some_list[:k])
for i in range (n):
    if max<sum(some_list[i:k+i]):
        max=sum(some_list[i:k+i])
    elif (some_list[-1]+some_list[0]+some_list[1])>max:
        max =(some_list[-1]+some_list[0]+some_list[1])
    elif (some_list[-2] + some_list[-1] + some_list[0]) > max:
        max = (some_list[-2] + some_list[-1] + some_list[0])
print(max)