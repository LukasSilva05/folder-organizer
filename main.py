import os
from tkinter.filedialog import askdirectory

os.system("cls")

caminho = askdirectory(title='teste')

lista_arquivos = os.listdir(caminho)

locais = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp"],
    "Documents": [".pdf"],
    "Programs": [".exe"],
    "Music": [".mp3"],
    "Video": [".mp4", ".mkv"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}') 