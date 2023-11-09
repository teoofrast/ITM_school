def proverka(a: int, b: int) -> bool:
    return f'{a >= 0 and b <= -2}'


print(proverka(int(input('Введите первое число: ')), int(input('Введите второе число: '))))