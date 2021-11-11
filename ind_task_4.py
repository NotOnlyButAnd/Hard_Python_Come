from math import sqrt


class Rectangle(object):
    id = "no_id"
    left_down_corner = (0.0, 0.0)
    right_upper_corner = (1.0, 1.0)

    def __init__(self, id, left_corn, right_corn):
        try:
            if left_corn[0] == right_corn[0] or left_corn[1] == right_corn[1]:
                raise ValueError("Углы находятся на одной линии!!!")
            else:
                self.id = id
                self.left_down_corner = left_corn
                self.right_upper_corner = right_corn
        except ValueError as Argument:
            print(f"\n!!!!!!!!ИСКЛЮЧЕНИЕ!!!!!!!!\n {Argument}")

    def square(self):
        return (self.right_upper_corner[0] - self.left_down_corner[0]) *\
               (self.right_upper_corner[1] - self.left_down_corner[1])

    def print_info(self):
        print(f'''\nRectangle info: \nID: {self.id}\nLeft down corner coordinate: {self.left_down_corner}
Right upper corner coordinate: {self.right_upper_corner}''')


class Pentagon(object):
    id = "no_id"
    vertexes = []

    def __init__(self, id, v1, v2, v3, v4, v5):
        try:
            self.id = id
            self.vertexes.append(v1)
            self.vertexes.append(v2)
            self.vertexes.append(v3)
            self.vertexes.append(v4)
            self.vertexes.append(v5)
            for i in range(len(self.vertexes)):
                for j in range(i, len(self.vertexes)):
                    if self.vertexes[i][0] == self.vertexes[j][0] and self.vertexes[i][1] == self.vertexes[j][1]:
                        raise ValueError("Упс! Две одинаковые точки!")
        except ValueError as Argument:
            print(f"\n!!!!!!!!ИСКЛЮЧЕНИЕ!!!!!!!!\n {Argument}")

    # по формуле гаусса
    def square(self):
        s1 = 0
        s2 = 0
        for i in range(0, 4):
            s1 += self.vertexes[i][0] * self.vertexes[i + 1][1]  # i-й икс и i + 1-й игрек
            s2 += self.vertexes[i + 1][0] * self.vertexes[i][1]  # i + 1-й икс и i-й игрек
        return 0.5 * abs(s1 + self.vertexes[4][0] * self.vertexes[0][1] -
                         s2 - self.vertexes[0][0] * self.vertexes[4][1])

    def print_info(self):
        print(f"\nPentagon info: \nID: {self.id}\nVertexes coordinates: {self.vertexes}")


# здесь могут быть объекты, для которых нет метода SQUARE - проверка нужна
def compare(obj1: Rectangle, obj2: Pentagon):
    sq1 = obj1.square()
    sq2 = obj2.square()
    if sq1 > sq2:
        print(f"\n{obj1.id} square ({sq1}) IS GREATER than {obj2.id} square ({sq2})")
    elif sq1 < sq2:
        print(f"\n{obj2.id} square ({sq2}) IS GREATER than {obj1.id} square ({sq1})")
    else:
        print(f"\n{obj1.id} and {obj2.id} squares are EQUAL ({sq1})")


# здесь нужна проверка, чтоб вершины именно вершинами были
def dist_2_vertex(vert_1, vert_2):
    return sqrt(pow(vert_2[0] - vert_1[0], 2) + pow(vert_2[1] - vert_1[1], 2))


def isInclude(rect: Rectangle, pent: Pentagon):
    flag = True
    # по сути, xmin = rect.left[0], xmax = rect.right[0]
    #          ymin = rect.left[1], ymax = rect.right[1]
    # с ними и надо сравнивать для проверки
    for vertex in pent.vertexes:
        if not (rect.left_down_corner[0] <= vertex[0] <= rect.right_upper_corner[0] and
                rect.left_down_corner[1] <= vertex[1] <= rect.right_upper_corner[1]):
            flag = False
    return flag


rect1 = Rectangle("rectangle_1", (0.0, 0.0), (0.0, 2.0))
rect1.print_info()
print(f"Square of {rect1.id}: {rect1.square()}")

rect2 = Rectangle("rectangle_2", (0.0, 0.0), (3.0, 2.0))
rect2.print_info()
print(f"Square of {rect2.id}: {rect2.square()}")

compare(rect1, rect2)

pent1 = Pentagon("pentagon_1", (0.0, 0.0), (0.0, 1.0), (1.0, 2.0), (3.0, 1.0), (0.0, 0.0))
pent1.print_info()
print(pent1.square())

compare(rect1, pent1)
compare(rect2, pent1)
print(f"\nis rect1 include pent1? -> {isInclude(rect1, pent1)}")
print(f"is rect2 include pent1? -> {isInclude(rect2, pent1)}")

rect3 = Rectangle("rectangle_3", (-1.0, -1.0), (4.0, 3.0))
rect3.print_info()
print(f"Square of {rect3.id}: {rect3.square()}")

print(f"\nis rect3 include pent1? -> {isInclude(rect3, pent1)}")
