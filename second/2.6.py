def leftandright(a: int) -> int:
    left = a // 10
    right = a % 10
    return f'{left} {right}'


print(leftandright(int(input('Введите двузначное число :'))))