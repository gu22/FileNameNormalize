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

# path_matricial = 'D:\Area de Teste - programação'



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
    global Dirs,Files
    Dirs = []
    sub_Dirs = []
    Files = []
    temp =[]
    put = os.walk(objetos)
    for diretorios,subdiretorios,arquivos in put:
        Dirs.append(diretorios)
        sub_Dirs.append(subdiretorios)
        Files.append(arquivos)
        # for i in ((range(len(Files)))-1)
    n_files = sum([len(item) for item in Files])
    return sub_Dirs, n_files
    

def AutoRename_files(lista,local):
    # global prep_list_arq
    # global prep_list_ext,nome
    index_file = 1
    
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
            # print(nome)
            # print(item_ext)
            original = (os.path.join(local,(f'{item_arq}{item_ext}')))
            output = (f'{nome}{item_ext}')
            # print(local)
            rename1 = (os.path.join(local,output))
            try:
                os.rename(original,rename1)
            except FileExistsError:
                rename2 = os.path.split(rename1)
                while os.path.exists(rename1):
                    output = (f'{rename2[1]}({index_file})')
                    rename1 = (os.path.join(rename2[0],output))
                    
                    index_file += 1
                os.rename(original,rename1)
                    
                
                
                
            # print (original)
            
                
                

def AutoRename_dir(local):
    
    index_folder = 1
    # folder = PurePath(local).name
    # base = os.path.dirname(local)
    folder = os.path.split(local)
    
    folder_normalize = unidecode(folder[1])
    folder_rename = os.path.join(folder[0],folder_normalize)
    
    if not folder_rename == folder[0]:
        try:
            os.rename(local,folder_rename)
        except FileExistsError:
            folder_rename2 = os.path.split(folder_rename)
            while os.path.exists(folder_rename):
                output = (f'{folder_normalize}({index_folder})')
                folder_rename = (os.path.join(folder_rename2[0],output))
                
                index_folder += 1
            os.rename(local,folder_rename)



#=========================================================

path_matricial = easygui.diropenbox(default='D:\Area de Teste - programação')

Indexacao(path_matricial)
z = Indexacao(path_matricial)

n_dirs =(len(Dirs))
# contador = (n_dirs -1)

for contagem in reversed(range(n_dirs)):
    
    # while contagem >= 0:
        # if not contador == 0:
        select_dir = Dirs[contagem]
        #     print("aceito")
        # else:
        #     print('pulei o 0')
        AutoRename_files(Files[contagem],select_dir)
        print(f'\n {contagem} ')
        # print(f'\n {contagem} | contador :{contador}')
        # contador-=1
        
for contagem in reversed(range(n_dirs)):
    if not contagem == 0:
        AutoRename_dir(Dirs[contagem])
        
    
    
    
    
print('ok')
