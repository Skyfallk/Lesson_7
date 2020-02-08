"""
Персональный счет.
Прогрмма имеет следующие функци:
1. Выводит состояние счета
2. Пополнить счет
3. Совершить покупку
   3.1. Ввести название покупки
   3.2. Ввести стоимость покупки
4. История покупок
5. Выход

При первом запуске на счету 0, история покупок чиста.
После закрытия итоговый счет и история покупок должны сохраниться в файл.
При последующих запусках программа должно загрузить информацию из файла.
"""
import os
import personal_bill_utils as utl

commands = ('Пополнить счет',
            'Соврешить покупку',
            'История покупок',
            'Выход')
base_dir = os.path.dirname(__file__)
#money = 0.0
#history = []
file_name = 'bill.txt'

money, history = utl.load_start_info(os.path.join(base_dir, file_name))


while True:
    print('Денег на счету:', money)
    for n, name in enumerate(commands):
        print(str(n+1) + '.', name)
    command = input('Введите номер команды:\n')
    if command == '4':
        # выход из программы
        # запись счета в файл
        my_file = open(file_name, 'w')
        my_file.write('Счет:' + str(money) + '\n')
        for buy in history:
            my_file.write('Название покупки:{}; стоимость:{}\n'.format(buy[0], buy[1]))
        break
    elif command == '1':
        # пополнение счета
        new_money = utl.chek_input('Введите сумму для пополнения счета:')
        money = utl.top_up(money, new_money)
    elif command == '2':
        # совершение покупки
        buy_name = input('Введите название покупки\n')
        buy_count = utl.chek_input('Введите стоимость покупки')
        if buy_count > money:
            print('Нехватает денег насчету.')
        else:
            history.append((buy_name, buy_count))
            money -= buy_count
    elif command == '3':
        # просмотр истории покупок
        for n, buy in enumerate(history):
            print(str(n+1) + '.', 'Название покупки', buy[0], 'Стоимость покупки', buy[1])
    else :
        print('В разработке')




