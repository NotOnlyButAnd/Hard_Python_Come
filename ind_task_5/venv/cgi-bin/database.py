import sqlite3
import os

# вывод названий всех таблиц БД через соединение con
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(f"\nTables: {cursorObj.fetchall()}")


# вывод всех строк из таблицы table через крусор cur
def select_all(cur, table):
    str = "SELECT * FROM " + table
    cur.execute(str)
    print(f"\n{table}: {cur.fetchall()}")


# Создание соедиения с базой
connection = sqlite3.connect("Environment.db")
# Создание курсора
cursor = connection.cursor()

# # Создание таблиц.
# тип
cursor.execute("""CREATE TABLE IF NOT EXISTS type_animal
                  (type_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  type_name VARCHAR(40),
                  description TEXT);
               """)
connection.commit()

# среда обитания
cursor.execute("""CREATE TABLE IF NOT EXISTS habitat
                    (habitat_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    habitat_name VARCHAR(30));
                """)
connection.commit()

#непосредственно животное
cursor.execute("""CREATE TABLE IF NOT EXISTS animal
                    (animal_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    animal_name VARCHAR(30),
                    description TEXT,
                    animal_type_ID INTEGER NOT NULL,
                    animal_habitat_ID INTEGER NOT NULL,
                    FOREIGN KEY (animal_type_ID) REFERENCES type_animal(type_ID),
                    FOREIGN KEY (animal_habitat_ID) REFERENCES habitat(habitat_ID));
                """)
connection.commit()

# # Исходные данные таблиц

# # обнуляем счетчик автоинкремента
# cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'type_animal';")
# cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'habitat';")
# cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'animal';")
# 
# cursor.execute("""INSERT INTO type_animal (type_name, description) VALUES
#                 ('Cat', 'Not friendly, lazy'),
#                 ('Dog', 'Friendly, activity'),
#                 ('Fish', 'Silent, wet')
#                """)
# connection.commit()
# 
# 
# cursor.execute("""INSERT INTO habitat (habitat_name) VALUES
#                 ('Forest'),
#                 ('House'),
#                 ('Jungle'),
#                 ('Africa')
#                """)
# connection.commit()
# 
# cursor.execute("""INSERT INTO animal (animal_name, description, animal_type_ID, animal_habitat_ID) VALUES
#                 ('Abessinian cat', 'A desert-colored cat, very beautiful', 1, 4),
#                 ('German shepherd', 'Very strong and smart dog', 2, 2),
#                 ('Сhihuahua', 'Small and very freaky dog', 2, 2)
#                """)
# connection.commit()
# 
# select_all(cursor, "type_animal")
# 
# select_all(cursor, "habitat")
# 
# select_all(cursor, "animal")

# Удаление всех строк из таблиц
# cursor.execute("""DELETE FROM type_animal
#                """)
# connection.commit()
#
# cursor.execute("""DELETE FROM habitat
#                """)
# connection.commit()
#
# cursor.execute("""DELETE FROM animal
#                """)
# connection.commit()
#
# select_all(cursor, "type_animal")
# select_all(cursor, "habitat")
# select_all(cursor, "animal")

# # Вывод всех собак из таблицы животные
# cursor.execute("SELECT animal_ID, animal_name, description, animal_type_ID, animal_habitat_ID FROM animal WHERE animal_type_ID = 2")
# print(f"\nAll dogs:: {cursor.fetchall()}")

# # Вывод всех животных но чтобы было видно не айди типов и сред обитания
cursor.execute("""SELECT animal.animal_ID, animal.animal_name, animal.description, animal.animal_type_ID, habitat.habitat_name
                   FROM animal JOIN habitat ON animal.animal_habitat_ID = habitat.habitat_ID""")
print(f"\nANIMALS!:: {cursor.fetchall()}")

# # ОБНОВЛЕНИЕ ТАБЛИЦЫ животные
# cursor.execute("UPDATE animal SET description = 'Undefinded' WHERE animal_ID = 25;")
# connection.commit()
# select_all(cursor, "animal")

# cursor.execute("SELECT * FROM type_animal")
# print(f"\nTypes of animals: {cursor.fetchall()}")
#
# cursor.execute("SELECT * FROM habitat")
# print(f"\nHabitats: {cursor.fetchall()}")

# вывод названий всех таблиц БД
sql_fetch(connection)


##################################
# ЭКСПОРТ В XML
##################################
import xml.etree.ElementTree as Etree

# Создание структуры файла
direct = os.path.abspath(__file__)
file = open(direct[:len(direct) - 11:] + 'Data.xml', 'w')

# Определение корня
data = Etree.Element('data')

###################################################################

# Определение таблицы Животное как потомка корня
table = Etree.SubElement(data, 'table')
table.set('name', 'animal')

# Извлечение данных из таблицы Животное
cursor.execute("SELECT * FROM animal")
animals = cursor.fetchall()

# Создание структуры записей как потомков таблицы Животное
for row in animals:
    entry = Etree.SubElement(table, 'entry')

    # Поля записи
    id = Etree.SubElement(entry, 'field')
    name = Etree.SubElement(entry, 'field')
    description = Etree.SubElement(entry, 'field')
    type = Etree.SubElement(entry, 'field')
    habitat = Etree.SubElement(entry, 'field')

    id.text = str(row[0])
    name.text = str(row[1])
    description.text = str(row[2])
    type.text = str(row[3])
    habitat.text = str(row[4])

###################################################################

# Определение таблицы Среда обитания как потомка корня
table = Etree.SubElement(data, 'table')
table.set('name', 'habitat')

# Извлечение данных из таблицы Среда обитания
cursor.execute("SELECT * FROM habitat")
habitats = cursor.fetchall()

# Создание структуры записей как потомков таблицы Среда обитания
for row in habitats:
    entry = Etree.SubElement(table, 'entry')

    # Поля записи
    id = Etree.SubElement(entry, 'field')
    name = Etree.SubElement(entry, 'field')

    id.text = str(row[0])
    name.text = str(row[1])

###################################################################

# Определение таблицы Вид животного как потомка корня
table = Etree.SubElement(data, 'table')
table.set('name', 'type_animal')

# Извлечение данных из таблицы Вид животного
cursor.execute("SELECT * FROM type_animal")
types = cursor.fetchall()

# Создание структуры записей как потомков таблицы Вид животного
for row in types:
    entry = Etree.SubElement(table, 'entry')

    # Поля записи
    id = Etree.SubElement(entry, 'field')
    name = Etree.SubElement(entry, 'field')
    description = Etree.SubElement(entry, 'field')

    id.text = str(row[0])
    name.text = str(row[1])
    description.text = str(row[2])

###################################################################

# Экспорт в файл
# какие-то два символа - b' - ставит в начале и при парсинге не может прочитать
# и еще в конце кавычка, поэтому ее тоже удаляем нафиг
# вручную насильно отрезаем их из table_data
table_data = str(Etree.tostring(data))
print(f"TABLE DATA: {table_data[2:len(table_data) - 1:]}")
file.write(table_data[2:len(table_data) - 1:])
file.close()

# вывод данных из таблиц до импорта из xml
print("\nДО ИМПОРТА :\n")
cursor.execute("SELECT * FROM animal")
print(f"animal: {cursor.fetchall()}")

cursor.execute("SELECT * FROM habitat")
print(f"habitat: {cursor.fetchall()}")

cursor.execute("SELECT * FROM type_animal")
print(f"type_animal: {cursor.fetchall()}")

# Импорт из файла
tree = Etree.parse(direct[:len(direct) - 11:] + 'Data.xml')
root = tree.getroot()

for table in root:
    if table.get('name') == 'animal':
        for entry in table:
            # id = entry[0].text
            name = entry[1].text
            description = entry[2].text
            type = entry[3].text
            habitat = entry[4].text
            cursor.execute("INSERT INTO animal(animal_name, description, animal_type_ID, animal_habitat_ID) VALUES(?, ?, ?, ?)",
                           (name, description, type, habitat))

    # почему-то здесь с одним столбцом не срабатывает нормально через валуес. пришлось колхозить
    elif table.get('name') == 'habitat':
        for entry in table:
            # id = entry[0].text
            name = entry[1].text
            query = "INSERT INTO habitat(habitat_name) VALUES ('" + name + "')"
            print(f"||||||{name}||||||{query}|||||||")
            cursor.execute(query)

    elif table.get('name') == 'type_animal':
        for entry in table:
            # id = entry[0].text
            name = entry[1].text
            description = entry[2].text
            cursor.execute("INSERT INTO type_animal(type_name, description ) VALUES(?, ?)", (name, description))

# вывод данных из таблиц ПОСЛЕ импорта из xml
print("\nПОСЛЕ ИМПОРТА :\n")
cursor.execute("SELECT * FROM animal")
print(f"animal: {cursor.fetchall()}")

cursor.execute("SELECT * FROM habitat")
print(f"habitat: {cursor.fetchall()}")

cursor.execute("SELECT * FROM type_animal")
print(f"type_animal: {cursor.fetchall()}")

connection.close()
