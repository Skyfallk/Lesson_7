"""
Напсать консольный файл-менеджер.

1. Создать папку
2. Удалить папку\файл
3. Копировать папку\файл
4. Просмотреть список содержимого в рабочей дирректории
5. Посмотреть только папки в р. дирректории
6. Посмотреть только файлы в р. дирректории
7. Сменить рабочую дирректорию
8. Посмотреть название ОС
9. Выход
"""

import os
import shutil
import sys

def print_files(func):
    def inner(*args, **kwargs):
        result = func(*args, *kwargs)
        for i, name in enumerate(result):
            print(str(i+1) + ')', name)

        return result
    return inner

def create_folder(folder_name, worked_dirrectory):
    """
    Создает папку с названием folder_name в диррекотории
    worked_dirrectory
    :param folder_name: str
    :param worked_dirrectory: str
    """
    # os.makedirs()
    try:
        os.mkdir(os.path.join(worked_dirrectory, folder_name))
        print("Папка успешно создана.")
    except FileExistsError:
        print('Папка уже существует')


def del_folder(folder_name, worked_dir):
    """
    Удаляет в рабочей дирректории папку или файл
    :param folder_name: имя папки\файла str
    :param worked_dir: полный путь к рабочей дирректории str
    """
    folder_path = os.path.join(worked_dir, folder_name)
    if os.path.isfile(folder_path):
        os.remove(folder_path)
        print('Файл успешно удален.')
    elif os.path.isdir(folder_path):
        os.rmdir(folder_path)
        print('Папка успешно удалена.')
    else:
        print('Нет такой папки\файла.')


# def copy_folder(worked_dir, folder_name):
#     res_dir = os.path.join(worked_dir, folder_name + '_copy')
#     shutil.copytree(os.path.join(worked_dir, folder_name), res_dir)
#     return res_dir

def copy_dir(name, worked_directory):
    name_path = os.path.join(worked_directory, name)
    # print('name_path',name_path)
    if os.path.isdir(name_path):
        shutil.copytree(name_path, name_path + '(copy)')
        print('Папка "{}" успешно скопирована.'.format(name))
        return name_path + '(copy)'
    elif os.path.isfile(name_path):
        f_name = os.path.basename(name_path)
        # print('f_name', f_name)
        # print('os.path.abspath(name_path)', os.path.abspath(name_path))
        res_dir = os.path.join(
            worked_directory, f_name[:f_name.index('.')] + '(copy)' + f_name[f_name.index('.'):]
        )
        shutil.copyfile(
            name_path,
            res_dir,
            follow_symlinks=True
        )
        print('Файл "{}" успешно скопирован.'.format(name))
        return res_dir
    else:
        print('Такой папки\\файла не существует')

@print_files
def get_listdir(worked_dir):
    return os.listdir(worked_dir)

@print_files
def get_folders_list(worked_directory):
    # folders_list = []
    # # print('<----------------- Папки ----------------->')
    # for name in os.listdir(worked_directory):
    #     if os.path.isdir(os.path.join(worked_directory, name)):
    #         folders_list.append(name)
    # # for i, name in enumerate(folders_list):
    #     print(str(i) + ')', name)
    # # print('<----------------------------------------->')

    # используем генератор списка
    return [name for name in os.listdir(worked_directory) if os.path.isdir(os.path.join(worked_directory, name))]

@print_files
def get_files_list(worked_directory):
    # files_list = []
    # print('<----------------- Файлы ----------------->')
    # for name in os.listdir(worked_directory):
    #
    #     if os.path.isfile(os.path.join(worked_directory, name)):
    #         files_list.append(name)
    # files_list.append(name) if os.path.isfile(os.path.join(worked_directory, name))

    # используем генератор списка
    return [name for name in os.listdir(worked_directory) if os.path.isfile(os.path.join(worked_directory, name))]


def change_worked_dir(new_dir):
    try:
        if os.listdir(new_dir):
            return new_dir

    except FileNotFoundError:
        return


def get_OS_info():
    return sys.platform + '(' + os.name + ')'


def save_listdir(worked_dir):
    file_list = get_files_list(worked_dir)
    folder_list = get_folders_list(worked_dir)
    file = open('worked_dir_info.txt', 'w')
    file.write('Files: ' + ','.join(file_list) + '\n')
    file.write('Folders: ' + ','.join(folder_list) + '\n')
    file.close()


if __name__ == '__main__':
    pass
