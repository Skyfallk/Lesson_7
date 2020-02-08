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

def create_folder(folder_name, worked_dirrectory):
    """
    Создает папку с названием folder_name в диррекотории
    worked_dirrectory
    :param folder_name: str
    :param worked_dirrectory: str
    """
    #os.makedirs()
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



# получить рабочую дирректорию текущую
#worked_dir = os.getcwd()
#new_folder = 'gogogo'
#new_folder_0 = '123'
#print(worked_dir)
#print(os.path.join(worked_dir, new_folder, new_folder_0))
#create_folder(new_folder, worked_dir)
#print('asd\\fdfv\\asdsad\q\\')
if __name__ == '__main__':
    print('Привет')