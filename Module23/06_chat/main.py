user_name = input('Введите имя пользователя: ')

while True:
    choice = int(input('Выберете действие. 1 - История чата, 2 - написать сообщение: '))
    if choice == 1:
        try:
            with open('history_chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('История чата пуста')
    elif choice == 2:
        new_message = input('Введите сообщение: ')
        with open('history_chat.txt', 'a') as file:
            file.write('{name}: {message}\n'.format(
                 name=user_name, message=new_message))
    else:
        print('Ты чего ввёл?')



