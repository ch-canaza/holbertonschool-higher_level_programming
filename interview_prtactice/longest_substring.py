#!/usr/bin/python3
""" my solution idk why is not working with some edege cases like  'qrsvbspk' """
s = "qrsvbspk"
# sub_str = []
# size_sub = 0
# max_sub = 0
# for i in s:
#     if i in sub_str:
#         sub_str.pop(0)
#         #sub_str.append(i)
#     if i not in sub_str:
#         sub_str.append(i)
#         print(sub_str) 
#         size_sub = len(sub_str)
#     if size_sub > max_sub:
#         max_sub = size_sub
# print(max_sub)

str_list = []
max_length = 0

for x in s:
    if x in str_list:
        str_list = str_list[str_list.index(x)+1:]
        #str_list = a list from repeated index+1 until end
        # "qrsvb's'pk" as 's' in str_list "qrsvb" returns 'v', 'p'
        print(str_list)
    str_list.append(x)    
    max_length = max(max_length, len(str_list))
    
print(max_length)
