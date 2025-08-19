import os
from tkinter.filedialog import askdirectory

# Limpa o terminal assim que o código for executado
os.system("cls")

# Abre o pop-up de selecão de pasta do Windows e armazena o caminho da pasta selecionada
caminho = askdirectory(title='teste')

# Armazena a lista de todos os arquivos armazenados na pasta selecionada
lista_arquivos = os.listdir(caminho)

# Dicionario com as pastas e extensões a serem organizadas
locais = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp"],
    "Documents": [".pdf"],
    "Programs": [".exe"],
    "Music": [".mp3"],
    "Video": [".mp4", ".mkv"]
}

# Itera todos os arquivos da pasta selecionada
for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}') 