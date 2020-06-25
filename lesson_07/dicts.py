
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

