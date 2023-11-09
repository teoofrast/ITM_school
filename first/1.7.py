def lengthandsquare(r: float) -> float:
    l = 2 * 3.14 * r
    s = 3.14 * r ** 2
    return f'Длина круга с радиусом {r} равна {l:.2f}, а площадь круга равна {s}'

print(lengthandsquare(5))