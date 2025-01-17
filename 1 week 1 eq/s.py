
import pandas
import operator


data = pandas.read_csv('titanic.csv', index_col='PassengerId')
res = data[:2]
res = data.head
# first Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
res = data['Sex'].value_counts()
# print(res)

# Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров.
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
# not_survived = data['Survived'].value_counts().get_value(0)
# survived = data['Survived'].value_counts().get_value(1)
# print(survived / (survived + not_survived))
# 0 : 549
# 1 : 342


# Какую долю пассажиры первого класса составляли среди всех пассажиров?
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен)
# all_class = data.count().get_value('Pclass')
# first_class = data['Pclass'].value_counts().get_value(1)
# print(first_class/all_class)
# print()
#   3    491
#   1    216
#   2    184

# Какого возраста были пассажиры?
# Посчитайте среднее и медиану возраста пассажиров.
# В качестве ответа приведите два числа через пробел.
# res = data['Age']
# print(res.mean())
# print(res.median())

# Коррелируют ли число братьев/сестер с числом родителей/детей?
# Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
# sisp = data['SibSp']
# parch = data['Parch']
# corr = sisp.corr(parch, method='pearson')
# # print(sisp)
# print(corr)

# Какое самое популярное женское имя на корабле?
# Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name).
# Это задание — типичный пример того, с чем сталкивается специалист по анализу данных.
# Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию.
# Попробуйте вручную разобрать несколько значений столбца Name и
# выработать правило для извлечения имен, а также разделения их на женские и мужские.
i = 0
res = data['Name'].get_values()
list_name = []
for name_row in res:
    is_woman = ("Miss." in name_row) or ("Mrs." in name_row)
    if is_woman:
        index_brace = name_row.find("(")
        if index_brace != -1:
            name_row = name_row[index_brace + 1:]
            index_space = name_row.find(" ")
            name_row = name_row[:index_space]
            list_name.append(name_row)
        else:
            index_point = name_row.find(".")
            name_row = name_row[index_point + 2:]
            index_space = name_row.find(" ")
            name_row = name_row[:index_space]
            list_name.append(name_row)
        # print(name_row)
        i += 1
        # print(res)
print(list_name)
dict_name = {}
dict_name["olo"] = 2
a = dict_name.get("olo")
for name in list_name:
    value = dict_name.get(name)
    if value is None:
        dict_name[name] = 1
    else:
        dict_name[name] = value + 1
sorted_x = sorted(dict_name.items(), key=operator.itemgetter(1))
print(sorted_x)