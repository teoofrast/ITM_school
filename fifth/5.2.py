def createdict():
    d = {
        'name': 'Azamat',
        'age': 32,
        'gender': 'male',
        'growth': 170,
        'weight': 88,
        'foot_size': 42,
    }
    return f'{d.get("name")} {d.get("age")} {d.get("gender")} {d.get("growth")} {d.get("weight")} {d.get("foot_size")}'


print(createdict())