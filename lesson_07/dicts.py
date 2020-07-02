
d = {}
print(type(d), d)
d = dict()
print(type(d), d)

"""
d  =  { 
    < ключ > :  < значение > , 
    < ключ > :  < значение > , 
      . 
      , 
      , 
    < ключ > :  < значение > 
}
"""

MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

print(MLB_team)

MLB_team = dict(
    [
        ('Colorado', 'Rockies'),
        ('Boston', 'Red Sox'),
        ('Minnesota', 'Twins'),
        ('Milwaukee', 'Brewers'),
        ('Seattle', 'Mariners')
    ]
)

print(MLB_team)

MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

print(MLB_team)

print(MLB_team['Boston'])
# print(MLB_team['Boston1'])
print(MLB_team.get('Boston', 'Нет такого города!'))

MLB_team['Odessa'] = 'Черноморец'
print(MLB_team)

MLB_team['Minnesota'] = 'Red bull'
print(MLB_team)

# len()
print(len(MLB_team))

# clear()
# MLB_team.clear()
# print(MLB_team)

# get(key, [default_value])
print(MLB_team['Boston'])
print(MLB_team.get('Boston', 'New team'))

# keys()
print(MLB_team.keys())

# values()
print(MLB_team.values())

# items()
print(MLB_team.items())
for key, value in MLB_team.items():
    print('key:', key, '\tvalue:', value)

# pop(key)
print(MLB_team.pop('Boston'))
print(MLB_team)

# popitem()
print(MLB_team.popitem())
print(MLB_team)

# update(new_dict)
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
print(d1)
print(d2)
d1.update(d2)
print(d1)
print(d2)

# fromkeys(list)
lst = [1, 2, 3, 4, 5, 6]
d = dict.fromkeys(lst)
print(d)