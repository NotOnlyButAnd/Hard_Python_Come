# Функция определения количества детей для узла дерева
# недо-рекурсивная, проходит всех возможных
# потомков узла elem в дереве tree (количество изначально 0)
def getCountChildren(tree, elem, count=0):
    if not elem in tree:
        # print('ok, thats all... ' + str(count))
        return count
    else:
        count += len(tree[elem])
        for i in tree[elem]:
            # print(i)
            count = getCountChildren(tree, i, count)
        return count

##############################################################
# основная программа
#############################################################

myFirstTree = {}    # Ключ - узел, значение - список потомков
nodes = []  # вообще все узлы дерева

inputFile = open('input.txt', 'r')

# читаем 1 строку и кол-во узлов дерева
line = inputFile.readline()
count_elems = int(line)
print('Count elems tree: ' + str(line))

line = inputFile.readline()
while line:
    # читаем из текущей строки пару сын-родитель
    cur_pair = line.split()
    # print(cur_pair)

    # засовываем узлы дерева во ВСЕ узлы (если надо)
    if not cur_pair[1] in nodes:
        nodes.append(cur_pair[1])
    if not cur_pair[0] in nodes:
        nodes.append(cur_pair[0])

    # теперь засовываем в дерево (если надо)
    if not cur_pair[1] in myFirstTree:
        myFirstTree[cur_pair[1]] = [cur_pair[0]]
    else:
        myFirstTree[cur_pair[1]].append(cur_pair[0])
    line = inputFile.readline()

# выводим дерево и закрываем файл исходный
print(myFirstTree)
inputFile.close()

# словарь с количеством детей для каждого узла дерева
countChild = {}
for node in nodes:
    countChild[node] = getCountChildren(myFirstTree, node)

# сортируем узлы по алфавиту
nodes = sorted(nodes)

# выводим пары узел - кол-во детей
print('\n')
for node in nodes:
    print(node + ' ' + str(countChild[node]))

# print('\nCount of children for Elizabeth: ')
# print(getCountChildren(myFirstTree, 'Elizabeth', 0))


