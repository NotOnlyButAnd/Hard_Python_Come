#ind_task1
N = int(input("Введите количество частиц: "))
i = 0
print("Вводите резульаты замеров скорости: ")
min1_e = 30001
min2_e = 30001

min1 = 30001
min2 = 30001

while i < N:
    cur_num = int(input())
    if cur_num % 2 == 0:
        if cur_num <= min1_e:
            min2_e = min1_e
            min1_e = cur_num
        elif cur_num <= min2_e:
            min2_e = cur_num
    elif cur_num % 2 != 0:
        if cur_num <= min1:
            min2 = min1
            min1 = cur_num
        elif cur_num <= min2:
            min2 = cur_num
    else:
        print("Фиг с ним")
    i += 1
print("min1_e ", min1_e, "; min2_e ", min2_e, "; min1_e + min2_e ", min1_e + min2_e)
print("min1 ", min1, "; min2 ", min2, "; min1 + min2 ", min1+min2)
