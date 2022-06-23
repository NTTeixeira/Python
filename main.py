import os

path = "D:\menutotvs"
os.chdir(path)
list_function = []
list_linha = []
list_all = []


def read_text_file(file_path):
    f = open(file_path, 'r')
    linhas = f.readlines()
    n = 0
    for linha in linhas:
        list_linha.append(linha)
        type = linhas[n].strip()
        function = linhas[n - 1].strip()
        if linha.count('<Function>U_'):
            list_all.append(file.strip() + ":   " + type)
        n = n + 1


for file in os.listdir():
    if file.endswith(".xnu"):
        file_path = f"{path}\{file}"
        read_text_file(file_path)




'''
characters = " "
for x in range(len(characters)):
    list_all = list_all.replace(characters[x])
    print(list_all)
'''
for y in list_all:
    y = y.rstrip('\n')
    print(y)
