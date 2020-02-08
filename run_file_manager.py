import os
import file_manager as fm

commands = ('Создать папку',
            'Удалить папку\\файл',
            'Копировать папку\\файл',
            'Просмотреть список содержимого в рабочей дирректории',
            "Посмотреть только папки в р. дирректории",
            'Посмотреть только файлы в р. дирректории',
            'Сменить рабочую дирректорию',
            'Посмотреть название ОС',
            'Выход')

while True:
    worked_dir = os.getcwd()
    for n, name in enumerate(commands):
        print(str(n+1) + '.', name)
    command = input('Введите номер команды:\n')
    if command == '9':
        break
    elif command == '1':
        name = input('Введите имя папки:\n')
        fm.create_folder(folder_name=name, worked_dirrectory=worked_dir)
    elif command == '2':
        name = input('Введите имя папки\\файла:\n')
        fm.del_folder(name, worked_dir)
    else :
        print('В разработке')