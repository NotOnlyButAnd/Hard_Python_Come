#!/usr/bin/python

# Импорт модулей для работы с CGI
import cgi, cgitb
import html
import sqlite3
import os


# вывод названий всех таблиц БД через соединение con
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(f"\nTables: {cursorObj.fetchall()}")


# Создание соедиения с базой
direct = os.path.abspath(__file__)
# print(f"\nDIRECTORY: {direct[:len(direct) - 15:]}")
connection = sqlite3.connect(direct[:len(direct) - 7:] + "Environment.db")
# Создание курсора
cursor = connection.cursor()

# Создание экземпляра FieldStorage
form = cgi.FieldStorage()

# Получение данных из полей
table = form.getvalue('Таблицы')
addTable = form.getvalue('table')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<meta charset=""UTF-8"">")
print ("<title align = 'center'> БД животные </title>")
print ("</head>")
print ("<body bgcolor = #E63244")
print ("<h1 align = 'left'>База данных животные (окружающая среда)</h1>")

# Форма выбора таблиц для вывода данных
print("""<form action = "/cgi-bin/View.py" method = "post">
<select name = "Таблицы">
<option value = "animal">Животные</option>
<option value = "habitat">Среды обитания</option>
<option value = "type_animal">Виды животных</option>
</select>
<input type = "submit" value = "Вывести" />
</form>""")

# Форма выбора таблиц для добавления данных
print("""<form action = "/cgi-bin/View.py" method = "post">
<input type = 'radio' name = 'table' value = 'animal' /> Животные <br>
<input type = 'radio' name = 'table' value = 'habitat' /> Среды обитания <br>
<input type = 'radio' name = 'table' value = 'type_animal' /> Виды животных <br>
<input type = "submit" value = "Добавить данные" />
</form>""")

# sql_fetch(connection)
# table = 'animal'

# Вывод таблиц на экран
if table == 'animal':
    # Запрос таблицы ЖИВОТНЫЕ
    cursor.execute("""SELECT animal.animal_ID, animal.animal_name, animal.description, type_animal.type_name, habitat.habitat_name
                   FROM animal 
                   JOIN habitat ON animal.animal_habitat_ID = habitat.habitat_ID
                   JOIN type_animal ON animal.animal_type_ID = type_animal.type_ID""")
    animals = cursor.fetchall()
    # print(f"\n\nANIMALS: {animals}")

    # Таблица СРЕДЫ ОБИТАНИЯ
    print("<table cellspacing = '10'>"
          "<caption><h2>Животные</h2></caption>"
          "<tr>"
          "<th>ID</th>"
          "<th>Название</th>"
          "<th>Описание</th>"
          "<th>Вид</th>"
          "<th>Среда обитания</th>"
          "</tr>")
    for row in animals:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
              "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3],
              "</td><td align = 'center'>", row[4], "</td></tr>")
    print("</table>")

elif table == 'habitat':
    # Запрос таблицы СРЕДЫ ОБИТАНИЯ
    cursor.execute("""SELECT habitat_ID, habitat_name 
                    FROM habitat""")
    habitats = cursor.fetchall()

    # Таблица СРЕДЫ ОБИТАНИЯ
    print("<table cellspacing = '10'>"
          "<caption><h2>Среды обитания</h2></caption>"
          "<tr>"
          "<th>ID</th>"
          "<th>Название</th>"
          "</tr>")
    for row in habitats:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1])
    print("</table>")

elif table == 'type_animal':
    # Запрос таблицы ВИДЫ ЖИВОТНЫХ
    cursor.execute("""SELECT type_ID, type_name, description
                    FROM type_animal""")
    types_animal = cursor.fetchall()

    # Таблица ВИДЫ ЖИВОТНЫХ
    print("<table cellspacing = '10'>"
          "<caption><h2>Виды животных</h2></caption>"
          "<tr>"
          "<th>ID</th>"
          "<th>Название</th>"
          "<th>Описание</th>"
          "</tr>")
    for row in types_animal:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
              "</td><td align = 'center'>", row[2])
    print("</table>")


# Добавление данных в таблицУ
if addTable == 'animal':

    print("""<form action = "/cgi-bin/View.py" method = "post">
    Название: <input type = "text" name = "animal_name" /> 
    Описание: <input type = "text" name = "description" />
    Вид животного (ID): <input type = "text" name = "type" />
    Среда обитания (ID): <input type = "text" name = "habitat" />
    <input type = 'submit' value = 'Добавить'>
    </form>""")

animal_name = form.getvalue('animal_name')
descript = form.getvalue('description')
type_name = form.getvalue('type')
habitat_name = form.getvalue('habitat')
# print(f"{animal_name}, {descript}, {type_name}, {habitat_name}")

cursor.execute("INSERT INTO animal(animal_name, description, animal_type_ID, animal_habitat_ID) VALUES(?, ?, ?, ?)",
                (animal_name, descript, type_name, habitat_name))
connection.commit()
addFlag = False

# elif addTable == 'habitat':
#     print("""<form action = "/cgi-bin/View.py" method = "post">
#         Название: <input type = "text" name = "habitat_name" />
#         <input type = 'submit' value = 'Добавить'>
#         </form>""")
#
#     # Получение данных из полей
#     habitat_name = form.getvalue('habitat')
#
#     cursor.execute("INSERT INTO habitat(habitat_name) VALUES(?)",
#                    (habitat_name))
#     connection.commit()
#
# elif addTable == 'type_animal':
#     print("""<form action = "/cgi-bin/View.py" method = "post">
#         Название: <input type = "text" name = "type_name" />
#         Описание: <input type = "text" name = "description" />
#         <input type = 'submit' value = 'Добавить'>
#         </form>""")
#
#     # Получение данных из полей
#     type_name = form.getvalue('type_name')
#     description = form.getvalue('description')
#
#     cursor.execute("INSERT INTO type_animal(type_name, description) VALUES(?, ?)",
#                    (type_name, description))
#     connection.commit()

# Получение данных из полей


print ("</body>")
print ("</html>")
