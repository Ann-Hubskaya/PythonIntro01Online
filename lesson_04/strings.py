s = """
f;gjer;lkjg're
qegmrel;kgjnerq
elkgner'jg
"""

'''

'''

"Hello World!"
'Hello World!'

# 0x26bd

# print(chr(0x26bd))
# print(chr(9917))
# print('\u26bd')
#
# print(ord('⚽'))
# print(hex(ord('⚽')))

# wave = '~'
# boat = '\U0001F6A3'
# seagull = '\u033C'
# fish = '\U0001F41F'
# penguin = '\U0001F427'
# wale = '\U0001F40B'
# octopus = '\U0001F419'
#
# row = wave * 10 + boat + wave * 15 + '\n'
# fish_row = wave * 4 + fish + wave * 21 + '\n'
# wale_row = wave * 10 + wale + wave * 15 + '\n'
# penguin_row = wave * 7 + penguin + wave * 18 + '\n'
# octopus_row = wave * 17 + octopus + wave * 8 + '\n'
#
# sea = row + fish_row + wale_row + penguin_row + octopus_row
# print(sea)

#        0  1  2  3  4      01234
#       'H  E  L  L  O'     HELLO
#       -5 -4 -3 -2 -1

# s = 'Hello World!'
# print(s[4], s[-8])
#
# """
#     string[start: stop: step]
# """
#
# s = 'Process finished with exit code 0'
# print(s[8:16:2])

# s = 'test string'
# print(s[1])         # e
# print(s[-1])        # g
# print(s[1:3])       # es
# print(s[1:-1])      # est strin
# print(s[1:len(s)-1])
# print(s[:3])        # tes
# print(s[2:])        # st string
# print(s[:-1])       # test strin
# print(s[::2])       # ts tig
# print(s[1::2])      # etsrn
# print(s[::-1])      # gnirts tset

"""
find('str', start, stop)
rfind
"""
s = 'Process finished with exit code 0'
# idx = s.find('i')
# print(idx)
# idx = s.find('i', idx+1)
# print(idx)
# idx = s.find('i', idx+1)
# print(idx)
# idx = s.find('i', idx+1)
# print(idx)
# idx = s.find('i', idx+1)
# print(idx)
#
# idx = 0
# while True:
#     idx = s.find('i', idx)
#     if idx < 0:
#         break
#     print(idx)
#     idx += 1

"""
replace('old', 'new', count)
"""
print(s.replace('s', 'A'))

"""
count('str', start, stop)
"""
print(s.count('i'))

"""
upper()
lower()
"""
print(s.upper())
print(s.lower())

"""
strip('str')
"""
txt = 'eeeeone two three four five six seven#######'
print("'" + txt + "'")
result = txt.strip('e').strip('#')
print("'" + result + "'")
