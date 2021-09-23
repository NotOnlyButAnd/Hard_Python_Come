# дана строка из слов с пробелами. для каждого слова посчитать сколько раз встречалось ранее в строке
# Найти слово кот чаще всего встречается. Если таких неск-ко, то вывести наименьшее (в лексикографич порядке)

# str = input()
#
# list = str.split()
# print(list)
# #set = set(list)
# voc = {}
# for i in list:
#     #print(i, list.count(i))
#     voc[i] = list.count(i)
# print(voc)
# max = max(voc.values())
# #print(max)
# list = []
# for i in voc.keys():
#     if voc.get(i) == max:
#         list.append(i)
# print(sorted(list)[0])


# даны пары слов все различные для заданного слова вывести его синоним
# list = input().split(',')
# print(list)
# dict = {}
# for i in list:
#     t = i.split()
#     dict[t[0]] = t[1]
# print(dict)
#
# word = input()
#
# for v, k in dict.items():
#     if word == v:
#         print(k)
#     elif word == k:
#         print(v)


#дан список стран и для каждой страны список городов для заданного города вывести страну в которой она находится

countries = input().split()
dict = {}
for i in countries:
    dict[i] = input().split()

print(dict)
word = input()

for k, v in dict.items():
    if word in v:
        print(k)
