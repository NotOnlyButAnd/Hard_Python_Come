# r'[\d][\d]\d\.[\d][\d]\d\.[\d][\d]\d\.[\d][\d]\d' - ip
# r'\d\d\:\d\d\:\d\d' - time
# r'[a-zA-Z]+' - day of week
# re.search (pattern, string)

ip_addresses = {}
time = {}
days = {'monday' : 0, 'tuesday' : 0, 'wednesday' : 0, 'thursday' : 0, 'friday' : 0, 'saturday' : 0, 'sunday' : 0}

input_file = file.open('input.txt','r')

while True:
    # считываем строку
    line = input_file.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    cur_ip = re.search(r'[\d][\d]\d\.[\d][\d]\d\.[\d][\d]\d\.[\d][\d]\d', line) 
    cur_time = re.search(r'\d\d\:\d\d\:\d\d', line)
    cur_day = re.search(r'[a-zA-Z]+', line)
    pri

# закрываем файл
input_file.close()
