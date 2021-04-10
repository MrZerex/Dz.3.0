def delen(a ,b):
    try:
        rez = a / b
        return rez
    except ZeroDivisionError:
        print('На ноль делить нельзя')

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

print(f'Результат деления {delen(num1, num2)}')