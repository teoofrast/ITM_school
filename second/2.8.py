def perestanovka(a: int) -> int:
    right = str(a // 10)
    left = str(a % 10)
    new = int(left + right)
    return new


print(perestanovka(int(input("Введите двузначное число: "))))