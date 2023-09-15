def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def func():
    while True:
        n1 = int(input('Введите первое число\n'))
        n2 = int(input('Введите второе число\n'))
        choise = int(input('Выберите действие: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, 5 - конец программы\n'))
        match choise:
            case 5:
                print('Press Entrer')
                input()
                break
            case 1:
                print(f'Выполняется сложение\n{add(n1, n2)}')
            case 2:
                print(f'Выполняется вычитание\n{sub(n1, n2)}')
            case 3:
                print(f'Выполняется умножение\n{mul(n1, n2)}')
            case 4:
                print(f'Выполняется деление\n{div(n1, n2)}')
            case _:
                print('error')


print(func())