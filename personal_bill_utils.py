import os

def top_up(money, summ):
    money += summ
    print('Счет пополнен на', summ)
    return money

def chek_input(question):
    while True:
        x = input(question + '\n')
        try:
            x = float(x)
            if x >= 0:
                return x
                break
            else:
                print('Введите положительное число')
        except ValueError:
            print('Введите число, не буквы')

def load_start_info(file_path):
    """
    Загружает из файла начальную информацию о счете
    :param file_path: путь к файлу str
    :return: состояние счета из файла float
    """
    history = []
    base_dir = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    #print(os.path.isfile(file_path))
    #print(base_dir, base_name)
    #print(os.listdir(base_dir))
    if base_name in os.listdir(base_dir):
        my_file = open(file_path, 'r')
        for n, line in enumerate(my_file):
            if n == 0:
                money = line[:-1]
                money = float(money.split(':')[1])
                #print(money)
            else:
                line = line[:-1]
                line = line.split(';')
                #print(line)
                buy_name = line[0].split(':')[1]
                buy_cost = float(line[1].split(':')[1])
                history.append((buy_name, buy_cost))
                #print(history)
        my_file.close()
        return money, history

    else:
        print('Файл с историей не обнаружен. Конфигурация начнется с нуля.')
        return 0.0, history





