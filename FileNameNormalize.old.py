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
contador = str(0)


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
    
# def Indexacao(objetos):
    # global x,y,z,r
    # global contador
    # nomeador  = f'Dir_{contador}'
    # for part in objetos:
    #     dir_check = os.path.join(local,part)
        
    #     if os.path.isdir(dir_check) is False:
    #         nomeador.append(os.path.join(local,part))
    #     else:
    #         pass
    # return nomeador
    
        # for i in os.scandir(objetos):
        #     # print(i)
        #     if i.is_dir():
        #         print(i)
        #         # print('ok\n')
        #         Indexacao(i)
            # else:
            #     print('nao')
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
        
              

# path_dir = easygui.fileopenbox()

# intodir = os.listdir(path)

# x = Vasculhar(path_matricial)

# print(x)

Indexacao(path_matricial)
# for i in os.scandir(path_matricial):
#     print(i)
#     if i.is_dir():
#         print(i)
#         print('ok\n')
#     else:
#         print('nao')

# for dot in intodir:
#     in_path = os.listdir(dot)