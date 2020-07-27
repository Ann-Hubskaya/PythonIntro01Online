# EOF - end of file

# test.txt
'''

'''

'''
root (/)
    └── Folder_1
            └── Folder_2
                    └──------- Folder_3
                    |               └── File_3_1.txt
                    └── File.csv    └── File_3_2.gif
'''

# import os
# print(os.sep)
#
# path = '/Folder_1/Folder_2/Folder_3/File_3_1.txt'

'''
.
..


../File.csv
'''


'''
\n\r    Windows
\n      Linux
\r      MacOS
'''

# file = open('file_name.exe', 'bw+', encoding='utf-8')

'''
r   (read) - default
w   (write)
x   (exclusive)
a   (append)

b   (binary)
t   (text) - default

+   (read/write)
'''

file = open('test.txt', 'w')

file.write('python.exe')

file.close()











