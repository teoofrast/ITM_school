def createdict():
    d = {
        'name': 'Azamat',
        'age': 32,
        'gender': 'male',
        'growth': 170,
        'weight': 88,
        'foot_size': 42,
    }

    d.setdefault('foot_size2', 41)
    return d

print(createdict())