def spisok():
    citylist = ["Ростов", "+", "на", "-", "Дону"]
    citylist[1] = '-'
    return f'{citylist[0]}{citylist[1]}{citylist[2]}{citylist[3]}{citylist[4]}'

print(spisok())