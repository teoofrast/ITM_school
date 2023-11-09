def lastandprelastcount(a: int) -> int:
    lastcount = a % 10
    prelastcount = a % 100 // 10
    return f'{lastcount} {prelastcount}'


print(lastandprelastcount(int(input("Введите трехзначное число: "))))