def volumeandsquare(a: float) -> float:
    v = a ** 3
    s = 6 * a ** 2
    return f'Объем куба со стороной {a} равен {v}, а площадь всех граней {s}'

print(volumeandsquare(2))