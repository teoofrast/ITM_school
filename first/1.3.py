def squareandperimetr(a: float, b: float) -> float:
    square = a * b
    perimetr = 2 * (a + b)
    return f'Площадь прямоугольника со сторонами {a} и {b} равна {square}, а периметр равен {perimetr}'


print(squareandperimetr(5, 3))