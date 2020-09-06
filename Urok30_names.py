from Urok30_Testirovanie import full_name

print('Для остановки теста введите q')

while True:
    first = input('\nВведи имя: ')
    if first == 'q':
        break
    last = input('\nВведи фамилию: ')
    if last == 'q':
        break

    format_name = full_name(first, last)
    print('\tФорматированное имя: ' + format_name)

