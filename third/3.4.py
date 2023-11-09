def proverka(a: int, b: int) -> bool:
    return f'{a > 2 and b <= 3}'


print(proverka(int(input('Введите первое число: ')), int(input('Введите второе число: '))))