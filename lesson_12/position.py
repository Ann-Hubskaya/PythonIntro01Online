# tell()
# seek()

file = open('test1.txt', 'w+')

print(file.tell())
file.write('D:\PROJECT\Python\HILLEL\PythonIntro01Online\venv\Scripts\python.exe')
print(file.tell())
file.seek(0)
print(file.tell())
s = file.read()
print(s)

file.close()


