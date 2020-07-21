# PYTHONPATH =

# import lesson_10.mod_1 as module_1
# from lesson_10.mod_1 import float_num, number as int_num, very_long_name_of_variable as vl_variable
# from lesson_10.mod_1 import print_list as print_mod_1
# from lesson_10.mod_3 import print_list as print_mod_3
# #
# #
# # print(lesson_10.mod_1.float_num)
# print(module_1.float_num)
# print(float_num)
# print(int_num)
#
# # print(very_long_name_of_variable)
# print(vl_variable)
#
# print_mod_3(None)
# print_mod_1(None)
#
# #
# # lesson_10.mod_1.print_list(lesson_10.mod_1.some_list)
# #
# # print(lesson_10.mod_1.__file__)
#
# print(dir())

# from lesson_10.mod_1 import print_list

# import importlib
# from time import sleep

import importlib, time

import lesson_10.sub_dir_1.mod_3 as module_3
time.sleep(5)
importlib.reload(module_3)
time.sleep(5)
importlib.reload(module_3)
time.sleep(5)
importlib.reload(module_3)
time.sleep(5)
importlib.reload(module_3)
time.sleep(5)
importlib.reload(module_3)
time.sleep(5)
importlib.reload(module_3)

a = 45435