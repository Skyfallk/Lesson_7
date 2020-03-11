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
            'Сохранить содержимое рабочей дирректории в файл',
            'Выход')
worked_dir = os.getcwd()
while True:
    print(worked_dir)
    for n, name in enumerate(commands):
        print(str(n+1) + '.', name)
    command = input('Введите номер команды:\n')
    if command == '10':
        break
    elif command == '1':
        name = input('Введите имя папки:\n')
        fm.create_folder(folder_name=name, worked_dirrectory=worked_dir)
    elif command == '2':
        name = input('Введите имя папки\\файла:\n')
        fm.del_folder(name, worked_dir)
    elif command == '3':
        name = input('Введите имя папки\\файла:\n')
        fm.copy_dir(name, worked_dir)
    elif command == '4':
        print(fm.get_listdir(worked_dir))
    elif command == '5':
        print('Папки:')
        for i, name in enumerate(fm.get_folders_list(worked_dir)):
            print(str(i) + ')', name)

    elif command == '6':
        print('Файлы:')
        for i, name in enumerate(fm.get_files_list(worked_dir)):
            print(str(i) + ')', name)
    elif command == '7':
        new_dir = input('Введите название новой рабочей дирректории')
        new_dir = fm.change_worked_dir(new_dir)
        if new_dir:
            worked_dir = new_dir
    elif command == '8':
        print(fm.get_OS_info())

    elif command == '9':
        fm.save_listdir(worked_dir)
    else :
        print('В разработке')