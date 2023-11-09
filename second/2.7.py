def sumandproizv(a: int) -> int:
    left = a // 10
    right = a % 10
    sum = left + right
    proizv = left * right
    return f'{sum} {proizv}'

print(sumandproizv(int(input('Введите двузначное число: '))))