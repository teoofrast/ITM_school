def schet(a: float, b: float) -> float:
    if a != 0 and b != 0:
        summa = a + b
        raz = a - b
        proizv = a * b
        chastnoekv = a ** 2 / b ** 2
        return f'Сумма чисел {a} и {b} равна {summa}, разность равна {raz}, произведение равно {proizv}, частное их квадратов равно {chastnoekv:.2f}'
    else:
        return f'Ошибка!!! Есть число равное нулю'

print(schet(5, 2))