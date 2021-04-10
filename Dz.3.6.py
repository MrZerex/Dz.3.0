def latin():
    new_str = ''
    lat = 'abcdefghijklmopqstuvwxyz'
    words = input('Введите слова латинскими буквами в нижнем регистре: ')
    words = words.split()
    for word in words:
        new_word = set(word) - set(lat)
        if len(new_word) == 0:
            new_str = new_str + word.title() + ' '
    print(new_str)

latin()