user_IP_list = input('Введите IP: ').split('.')
if len(user_IP_list) != 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    for num in user_IP_list:
        if (not num.isdigit()) and num.isalnum():
            print(f'{num} - не целое число')
            break
        elif int(num) > 255:
            print(f'{num} превышает 255')
            break
        elif int(num) < 0:
            print(f'{num} меньше 0')
            break
    else:
        print('IP-адрес корректен')
