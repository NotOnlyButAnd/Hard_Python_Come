# дана строка из слов с пробелами. для каждого слова посчитать сколько раз встречалось ранее в строке
# Найти слово кот чаще всего встречается. Если таких неск-ко, то вывести наименьшее (в лексикографич порядке)

str = input()

list = str.split()
print(list)
#set = set(list)
voc = {}
for i in list:
    #print(i, list.count(i))
    voc[i] = list.count(i)
print(voc)
max = max(voc.values())
#print(max)
list = []
for i in voc.keys():
    if voc.get(i) == max:
        list.append(i)
print(sorted(list)[0])
