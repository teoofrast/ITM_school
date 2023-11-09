def neravenstvo(a: int, b: int, c:int) -> bool:
    return f'{a < b < c or a > b > c}'

print(neravenstvo(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))