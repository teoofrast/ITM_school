def squareandvolume(a: float, b: float, c: float) -> float:
    v = a * b * c
    s = 2 * (a * b + b * c + a * c)
    return f'Объем прямоугольного параллелепипеда со сторонами {a}, {b} и {c} равен {v}, а площадь всех граней равна {s}'

print(squareandvolume(1, 2, 3))