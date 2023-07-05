'''
Задание №7
Погружение в Python | Коллекции
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
'''


string = input("введите текст")
my_set = set(string)
my_dict_1 = {}
my_dict_2 = {}
my_dict_3 = {}
my_dict_4 = {}


for i in my_set:
    my_dict_1.setdefault(i, string.count(i))
print(my_dict_1)

count = 0
for i in my_set:
    for j in range(len(string)):
        if string[j] == i:
            count +=1
    my_dict_2[i] = count
    count = 0
print(my_dict_2)


