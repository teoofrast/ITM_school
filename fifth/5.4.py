def createdict():
    d = {
        'name': 'Azamat',
        'age': 32,
        'gender': 'male',
        'growth': 170,
        'weight': 88,
        'foot_size': 42,
    }

    d.pop('age')
    return d

print(createdict())