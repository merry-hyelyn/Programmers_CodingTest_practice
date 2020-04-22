# 기능 : ls, mkdir, cd, pwd

# os 모듈
# pws = os.system("pwd")
#     = os.getcwd()

# ls = os.listdir()
#    = os.system("ls")

# cd = os.chdir(path)

# mkdir = os.mkdir("파일명")
#       = os.system("mkdir [파일명]")

import os

print("==========START==========")
while True:
    os.system("pwd")
    print("""
    1. File list
    2. Change directory
    3. Make directory
    4. exit
    """)

    todo = int(input())

    if todo == 1:
        os.system("ls")

    elif todo == 2:
        os.chdir(input("Input Path : "))
    elif todo == 3:
        os.mkdir(input("Input file name: "))
    else:
        break
    print()
