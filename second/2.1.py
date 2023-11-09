def metrs(a: int) -> int:
    metr = a // 100
    return f'В {a} сантиметрах есть {metr} метра/ов'

print(metrs(int(input('Введите расстояние в сантиметрах: '))))