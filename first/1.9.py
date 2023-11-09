def sredgeom(a: float, b: float) -> float:
    if a >= 0 and b >= 0:
        sr = (a + b) ** (1 / 2)
        return f'Среднее геометрическое двух чисел {a} и {b} равно {sr:.2f}'
    else:
        return f'Ошибка!!! Среди {a} и {b} есть отрицательные числа'


print(sredgeom(25, 75))