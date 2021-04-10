def my_func(num1, num2, num3):
    list_num = [num1, num2, num3]
    list_num.remove(min(list_num))
    if list_num[0] > list_num[1]:
        print(f'Число {list_num[0]} больше числа {list_num[1]}')
    elif list_num[0] < list_num[1]:
        print(f'Число {list_num[0]} меньше числа {list_num[1]}')
    else:
        print(f'Числа равны')

numb1 = int(input('Введите первое число: '))
numb2 = int(input('Введите второе число: '))
numb3 = int(input('Введите третье число: '))

my_func(numb1, numb2, numb3)