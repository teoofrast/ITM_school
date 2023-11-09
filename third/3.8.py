def nechet(a: int, b: int) -> bool:
    return f'{a % 2 != 0 and b % 2 != 0}'


print(nechet(int(input('Введите первое число: ')), int(input('Введите второе число: '))))