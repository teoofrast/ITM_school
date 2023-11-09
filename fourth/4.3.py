def sortalphasanddigits():
    spisok = ["a", "s", "1", "a", "32", "23"]
    bukvy = [i for i in spisok if i.isalpha()]
    numbers = [int(i) for i in spisok if i.isdigit()]
    return f'{bukvy} {numbers}'


print(sortalphasanddigits())