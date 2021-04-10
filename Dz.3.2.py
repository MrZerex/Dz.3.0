def my_data (nam, fam, yer, cit, mail, phn):
    print(f'Ваше имя - {nam}, Ваша фамилия - {fam}, год рождения - {yer}, город проживания - {cit}, '
          f'Ваш e-mail - {mail}, Ваш номер телефона - {phn}')

name = input('Введите Ваше имя: ')
family = input('Введите Вашу фамилию: ')
year = input('Введите год Вашего рождения: ')
city = input('Введите Ваш город рождения: ')
e_mail = input('Введите Ваш e-mail: ')
phone = input('Введите Ваш номер телефона: ')

my_data(nam=name, fam=family, yer=year, cit=city, mail=e_mail, phn=phone)