# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

def most_frequent(text: str) -> list[str]:
    dict_counts = {}
    SHOW_LIMIT = 10
    new_sorted_dictionary = {}
    new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower(). \
        strip()
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        dict_counts[word] = counter
    sorted_values = sorted(dict_counts.values())[::-1]
    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dictionary[k] = dict_counts[k]
    return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]


text = 'История штата Луизиана прослеживается с тех периодов, когда она впервые была заселена человеком. ' \
       'Первое известное науке поселение появилось в Луизиане примерно 5500 лет назад. ' \
       'В 1763 году Франция уступила Луизиану Испании. Позже она снова перешла во владение Франции, но в 1803 году Французская Луизиана была продана США.' \
       ' 30 апреля 1812 года Луизиана стала 18-м штатом США. ' \
       'В том же году началась война с Англией, финальным сражением которой стала Битва за Новый Орлеан.'

print(most_frequent(text))