from PySimpleGUI import PySimpleGUI as sg
import shutil
import os
from glob import glob
from data import images

working_directory = 'C:/Chef/'
src_dir = 'C:/Chef/NFCe/Gerados/'

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Mês:'), sg.Combo(['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'], key= 'mes')],
    [sg.Text('Salvar em:')], [sg.InputText(key='caminho'),
    sg.FolderBrowse(initial_folder=working_directory)],
    [sg.Button('Gerar')]
]
#janela
window = sg.Window('NFe Emitidas', icon=images).Layout(layout)

#ler eventos
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Gerar':
        if value['mes'] == 'jan':
            mes = '01'
        elif value['mes'] == 'fev':
            mes = '02'
        elif value['mes'] == 'Mar':
            mes = '03'
        elif value['mes'] == 'Abr':
            mes = '04'
        elif value['mes'] == 'Mai':
            mes = '05'
        elif value['mes'] == 'Jun':
            mes = '06'
        elif value['mes'] == 'Jul':
            mes = '07'
        elif value['mes'] == 'Ago':
            mes = '08'
        elif value['mes'] == 'Set':
            mes = '09'
        elif value['mes'] == 'Out':
            mes = '10'
        elif value['mes'] == 'Nov':
            mes = '11'
        elif value['mes'] == 'Dez':
            mes = '12'
        else:
            print('Deu ruim!')

    desk = value['caminho'] + '/'
    print('Achei o caminho')

    isExist = os.path.exists(desk+'NFe XML')
    print('Achei a pasta')

    if not isExist:
        os.makedirs(desk+'NFe XML')
        print('Criei a pastinha!')

    for file in os.listdir(src_dir):
        if file.startswith("3122" + mes):
            shutil.copy2(src_dir+file, desk+'NFe XML')

    os.chdir(desk)
    print(os.getcwd())

    shutil.make_archive('NFe'+mes+'22','zip', desk, 'NFe XML')
    shutil.rmtree(desk+'NFe XML')
    print('Finalizado')

        