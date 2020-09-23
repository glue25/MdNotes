import re
from utilities import find_str_from_file,find_str_from_files

L = find_str_from_files('[ab][ab]',['tt.txt'], show_row=True, useRE=True)
for i in L:
    print(i)
# print(L)

