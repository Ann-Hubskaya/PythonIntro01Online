
# def fahrenheit(temperature):
#     return round(((float(9)/5)*temperature + 32), 2)


# def celsius(temperature):
#     return round((float(5)/9)*(temperature-32), 2)


temperatures = (36.5, 37, 37.5, 36.4, 36.8, 37.1, 38, 39)
# lst = []
# for t in temperatures:
#     lst.append(fahrenheit(t))
#
# print(lst)

# map(func, collection) ===> map
# list(map)

# F = map(fahrenheit, temperatures)
# l = list(F)
# print(l)
# C = map(celsius, l)
# print(tuple(C))

# temperatures_in_fahrenheit = list(map(fahrenheit, temperatures))
# temperatures_in_celsius = list(map(celsius, temperatures_in_fahrenheit))
# print(temperatures_in_fahrenheit)
# print(temperatures_in_celsius)

result = list(map(lambda temp: round(((float(9)/5)*temp + 32), 2), temperatures))
print(result)

result = list(map(lambda temp: round((float(5)/9)*(temp-32), 2), result))
print(result)

result = tuple(map(lambda temp: 'Height' if temp > 37 else 'Normal', result))
print(result)

