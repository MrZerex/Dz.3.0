def two_number (num1, num2):
    rez = 1
    for el in range(abs(num2)):
        rez *=  1 / num1
    print(f'{num1} в степени {num2} равно {rez}')

while True:
    number1 = float(input('Введите действительное положительное число: '))
    number2 = int(input('Введите целое отрицательное число: '))
    if number1 <= 0 or number2 >= 0:
        print('Ошибка. Введите действительное положительное число и целое отрицательное число')
        continue
    else:
        break

two_number(number1, number2)
