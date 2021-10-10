# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:26:12 2021

@author: gusan
"""

import os
import os.path
import easygui

import configparser
import sys
import pendulum

from unidecode import unidecode
from pathlib import PurePath
from datetime import datetime

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# path_matricial = 'D:\Area de Teste - programação'

config = configparser.ConfigParser(interpolation=None)
config.read('Config\Config.ini',encoding='utf-8')

caracteres_coringas = (config['DEFAULT']['Caracteres'])
diretorio_padrao = (config['DEFAULT']['Diretorio_padrao'])




class Logger(object):
    
    
    def __init__(self):
        
        self.terminal = sys.stdout

    def write(self, message):
        time1 = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
        with open (f"logfile-{time1}.log", "a") as self.log:            
            self.log.write(message)
        self.terminal.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass  

sys.stdout =  Logger()


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('.\Config\Face.ui', self)
        
        # self.setFixedSize(316, 357)
        # self.setWindowIcon(QtGui.QIcon('.\Config\Icon.ico'))
        
        
        self.nome_pasta.setText(diretorio_padrao)
        

        self.selecionar_pasta.clicked.connect(self.select_path)
        self.botao_iniciar.clicked.connect(self.msg)
        
        

        self.show()

    def msg(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setWindowTitle("ALERTA")
        msgBox.setText("Este Software irá renomear todos os arquivos\nApós Iniciar não é possivel interromper\n\nClique OK para continuar e Cancel para retornar para tela inicial ")
        
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.Principal()
            # print(self.nome_pasta.text())
        else:
            print('Cancel')
            
            

    def select_path(self):
        
        path_matricial = easygui.diropenbox(default=diretorio_padrao)
        self.nome_pasta.setText(path_matricial)
    
    def Principal(self):
        
        path_matricial= self.nome_pasta.text()
    #============================== funções ====================
        
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
            global datatempo
            # global prep_list_arq
            # global prep_list_ext,nome
            index_file = 1
            
            prep_list_arq = []
            prep_list_ext = []
            
            exclude = caracteres_coringas
            
            # print(f'\n ---{lista}----\n')
            for arq in lista:
                sep =os.path.splitext(arq)
                prep_list_arq.append(sep[0])
                prep_list_ext.append(sep[1])
                
            pacote = zip(prep_list_arq,prep_list_ext)
            for item_arq,item_ext in pacote:
                nome = unidecode(item_arq) 
                if nome == item_arq:
                    # print(f'\n{local}\n{nome}\n')
                    
                    
                    pass
                else:
                    # print(nome)
                    # print(item_ext)
                    original = (os.path.join(local,(f'{item_arq}{item_ext}')))
                    output = (f'{nome}{item_ext}')
                    for out in exclude:
                        output = output.replace(out,'_')
                    # print(local)
                    rename1 = (os.path.join(local,output))
                    try:
                        os.rename(original,rename1)
                        print(f"OK[FILE] -- {original}")
                    except FileExistsError:
                        rename2 = os.path.split(rename1)
                        sep =os.path.splitext(rename2[1])
                        while os.path.exists(rename1):
                            output = (f'{sep[0]} ({index_file}){sep[1]}')
                            rename1 = (os.path.join(rename2[0],output))
                            
                            index_file += 1
                        os.rename(original,rename1)
                    except PermissionError:
                         # print(f"{rename1} não foi possivel modificar ")
                        msg = (f"(ARQUIVO) {original} >> não foi possivel renomear, SENDO UTILIZADO PELO SISTEMA\n ")
                        with open(f'FAIL-{datatempo}.txt','a',encoding = 'utf-8') as fail_log:
                            fail_log.write(msg)
                            print(f"FAIL[FILE][System load] -- {original}")
                        continue
                    except:
                         # print(f"{rename1} não foi possivel modificar ")
                        msg = (f"(ARQUIVO) {original} >> não foi possivel renomear,NÃO IDENTIFICADO VERIFICAR LOG\n ")
                        with open(f'FAIL-{datatempo}.txt','a',encoding = 'utf-8') as fail_log:
                            fail_log.write(msg)
                            print(f"FAIL[FILE][unknown] -- {original}")
                        continue
                        
                        
                        
                    # print (original)
                    
                        
                        
        
        def AutoRename_dir(local):
            global datatempo
            index_folder = 1
            exclude = caracteres_coringas
            # folder = PurePath(local).name
            # base = os.path.dirname(local)
            folder = os.path.split(local)
            
            folder_normalize = unidecode(folder[1])
            for out in exclude:
                folder_normalize = folder_normalize.replace(out,'_')
            
            folder_rename = os.path.join(folder[0],folder_normalize)
            
            if not folder_rename == folder[0]:
                try:
                    os.rename(local,folder_rename)
                    print(f"OK [DIR] -- {local}")
                except FileExistsError:
                    folder_rename2 = os.path.split(folder_rename)
                    while os.path.exists(folder_rename):
                        output = (f'{folder_normalize}({index_folder})')
                        folder_rename = (os.path.join(folder_rename2[0],output))
                        
                        index_folder += 1
                    os.rename(local,folder_rename)
                except PermissionError:
                    # print(f"{folder_rename} não foi possivel modificar ")
                    msg = (f"(DIRETORIO) {local} >> não foi possivel renomear, SENDO UTILIZADO PELO SISTEMA\n ")
                    with open(f'FAIL-{datatempo}.txt','a',encoding = 'utf-8') as fail_log:
                        fail_log.write(msg)
                        print(f"FAIL[DIR][System load] -- {local}")
                    pass
                except PermissionError:
                    # print(f"{folder_rename} não foi possivel modificar ")
                    msg = (f"(DIRETORIO) {local} >> não foi possivel renomear, NÃO IDENTIFICADO VERIFICAR LOG\n ")
                    with open(f'FAIL-{datatempo}.txt','a',encoding = 'utf-8') as fail_log:
                        fail_log.write(msg)
                        print(f"FAIL[DIR][unknown] -- {local}")
                    pass
                
                
    #===============================[ Rotina principal ]==========================
                
        global diretorio_padrao,datatempo
        datatempo = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
        
        A = pendulum.now()
        print(f'========= Iniciado ====== {datatempo} =======\n')
        # path_matricial = easygui.diropenbox(default='D:\Area de Teste - programação')
        # path_matricial = easygui.diropenbox(default=diretorio_padrao)
        
        Indexacao(path_matricial)
        z = Indexacao(path_matricial)
        
        n_dirs =(len(Dirs))
        # contador = (n_dirs -1)
        print(f'========= [FILES] =============\n')
        for contagem in reversed(range(n_dirs)):
            
            # while contagem >= 0:
                # if not contador == 0:
                select_dir = Dirs[contagem]
                #     print("aceito")
                # else:
                #     print('pulei o 0')
                AutoRename_files(Files[contagem],select_dir)
                # print(f'\n {contagem} ')
                # print(f'\n {contagem} | contador :{contador}')
                # contador-=1
                
        print(f'\n========= [DIR] =============\n')
        for contagem in reversed(range(n_dirs)):
            if not contagem == 0:
                AutoRename_dir(Dirs[contagem])
        
        B = pendulum.now()
        delta = (B-A).seconds
        print(f'\n========= Finalizado - OK ====== Tempo decorrido: {delta} seg ====== {datatempo} =======\n')
    

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = Ui()
app.exec_()