# Дана строка (возможно, пустая),состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB Нужно написать функцию RLE, которая на выходе даст строку вида
# : A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку , если на вход пришла невалидная строка.Пояснения:
# Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза
# , к нему добавляется количество повторений.

string = input("Введите строку, состоящую из букв a-z ")
if not string.isalpha():
    print("Oшибка: строка должна состоять из букв!")
else:
    result = ""
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            if count > 1:
                result += string[i] + str(count)
                count = 1
            else:
                result += string[i]
    result += string[-1] + str(count)
    print(result)
