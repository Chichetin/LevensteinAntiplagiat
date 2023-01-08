import ast
import re


def file_cleaner(file):
    file = file.replace('\'', '\"')
    pattern = r"\"\"\"[^\"\"\"]*\"\"\""
    tri_kavichki = re.findall(pattern, file)
    for s in tri_kavichki:
        file = file.replace(s, '')
    return file


def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


def id_remover(str):
    pattern = r"id='[^']*'"
    ids = re.findall(pattern, str)
    for s in ids:
        str = str.replace(s, '')
    return str


def plagiat(file1, file2):
    file1 = file_cleaner(file1)  # это чтоб когда я буду менять переменные по ' - не упал никакой хуйни
    file2 = file_cleaner(file2)
    str1 = ast.dump(ast.parse(file1))
    str2 = ast.dump(ast.parse(file2))

    print("Вы хотите учитывать различие в названии переменных? 1/0")
    if (input() == '1'):
        str1 = id_remover(str1)
        str2 = id_remover(str2)
    rast = levenstein(str1, str2)
    if rast == 0:
        print("Коды - чистый плагиат!")
    else:
        length = len(file1)
        words = len(file1.split(" "))
        sred_bukv = length/words
        slov_narisovali = rast/sred_bukv
        print("Количество слов - ", words, ", среднее количество знаков - ", sred_bukv, ", расстояние Левенштейна - ", rast)
        print("Примерное количество слов разделяющие первые текст и второй - ", slov_narisovali, "\n")

file = open(input())

count = 0
while True:
    count += 1
    line = file.readline()
    if not line:
        break
    mass = line.split(" ")
    print(mass)
    file1 = open(mass[0].strip()).read()
    file2 = open(mass[1].strip()).read()
    print("Процесс пошёл!")

    plagiat(file1, file2)


