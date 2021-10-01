# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:26:12 2021

@author: gusan
"""

import os
import os.path
import easygui


import shutil
from shutil import copytree

from unidecode import unidecode
from pathlib import PurePath

path_matricial = 'D:/gusan/Documents/PROGRAMAÇÃO/GitHub/FileNameNormalize/teste'



def Vasculhar(diretorio_observado):
    dentro_diretorio = os.listdir(diretorio_observado)
    return dentro_diretorio

# def Escavador(olheiro):
#     for dots in olheiro:
#         dir_check = os.path.join(path_name,dots)
#         if os.path.isdir(dir_check) is False:
#             files.append(os.path.join(path_name,i))
#         else:
#             pass
#     return files
    

def Indexacao(objetos):
    global Dirs,sub_Dirs,Files
    Dirs = []
    sub_Dirs = []
    Files = []
    put = os.walk(objetos)
    for diretorios,subdiretorios,arquivos in put:
        Dirs.append(diretorios)
        sub_Dirs.append(subdiretorios)
        Files.append(arquivos)

def AutoRename_files(lista,local):
    global prep_list_arq
    global prep_list_ext,nome
    
    prep_list_arq = []
    prep_list_ext = []
    print(f'\n ---{lista}----\n')
    for arq in lista:
        sep =os.path.splitext(arq)
        prep_list_arq.append(sep[0])
        prep_list_ext.append(sep[1])
        
    pacote = zip(prep_list_arq,prep_list_ext)
    for item_arq,item_ext in pacote:
        nome = unidecode(item_arq) 
        if nome == item_arq:
            print(f'\n{local}\n{nome}\n')
            
            
            pass
        else:
            print(nome)
            print(item_ext)
            print(f'{nome}{item_ext}')
            print(local)
            # os.rename()

#=========================================================

# path_dir = easygui.fileopenbox()

Indexacao(path_matricial)

n_dirs =(len(Dirs))
contador = (n_dirs -1)

for contagem in range(n_dirs):
    
    while contador >= 0:
        # if not contador == 0:
        select_dir = Dirs[contador]
        #     print("aceito")
        # else:
        #     print('pulei o 0')
        AutoRename_files(Files[contador],select_dir)
        print(f'\n {contagem} | contador :{contador}')
        contador-=1
        
print('ok')
