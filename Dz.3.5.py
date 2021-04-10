def summ():
    summ = 0
    while True:
        check = 0
        num = input('Введите числа, разделенные пробелом (Введите "!" для выхода): ')
        num = num.split()
        for el in num:
            if el == '!':
                check = 1
                break
            summ += float(el)
        print(f'Сумма чисел равна: {summ}')
        if check == 1:
            break

summ()