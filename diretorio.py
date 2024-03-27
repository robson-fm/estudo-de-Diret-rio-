import tkinter as tk
from tkinter import filedialog

# Definir o caminho desejado
diretorio = "C:/Teste_ProjetoSimulador"


def abrir_arquivo():
    global diretorio
    # Abre uma caixa de diálogo para selecionar um arquivo
    escolherArquivo = filedialog.askopenfilename(initialdir=diretorio)

    print(escolherArquivo)

    # Verificar se o arquivo selecionado está dentro do caminho desejado
    if escolherArquivo.startswith(diretorio):
        # Se o arquivo estiver no caminho desejado, prosseguir com o processamento do arquivo
        print("Arquivo selecionado:", escolherArquivo)
        # Aqui você pode fazer o que precisa com o arquivo selecionado
    else:
        # Se o arquivo não estiver no caminho desejado, mostrar uma mensagem de aviso na tela
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showwarning("Aviso", "Caminho do arquivo incorreto")
        # Chamar a função novamente para permitir que o usuário selecione outro arquivo
        abrir_arquivo()

# Exemplo de uso
root = tk.Tk()
root.withdraw()  # Esconder a janela principal

abrir_arquivo()



