import tkinter as tk
from tkinter import messagebox
from pytubefix import YouTube
import os


# Função para iniciar o download
def iniciar_download():
    link = link_entry.get()  # Obtém o link do vídeo a partir do campo de entrada
    escolha = escolha_var.get()  # Obtém a escolha entre MP4 ou MP3

    if link == "" or link == placeholder:  # Verifica se o link foi preenchido
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo!")
        return

    try:
        yt = YouTube(link)
        print(f"Título do vídeo: {yt.title}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar o vídeo: {e}")
        return
    
# Baixando em MP4
    if escolha == "MP4":
        ys = yt.streams.get_highest_resolution()
        caminho_download = "C:/Users/alexl/Downloads"
     
# Baixa o arquivo
        arquivo_baixado = ys.download(output_path="C:/Users/alexl/Downloads")

# Obtém o nome do arquivo baixado
        nome_arquivo = os.path.basename(arquivo_baixado)
        novo_nome = os.path.splitext("𓅔Lucio.Downloader𓅔 " + nome_arquivo)[0] + ".mp4" # Aciciona minha marca e nome
        novo_arquivo = os.path.join(caminho_download, novo_nome)
     
# Renomeia o arquivo
        os.rename(arquivo_baixado, novo_arquivo)

        messagebox.showinfo("Sucesso", "Download do vídeo em MP4 concluído!")

# Baixando em MP3
    elif escolha == "MP3":
        ys = yt.streams.filter(file_extension='mp4').get_audio_only()
        caminho_download = "C:/Users/alexl/Downloads"

# Baixa o arquivo
        arquivo_baixado = ys.download(output_path="C:/Users/alexl/Downloads")

# Obtém o nome do arquivo baixado
        nome_arquivo = os.path.basename(arquivo_baixado)
        novo_nome = os.path.splitext("𓅔Lucio.Downloader𓅔 " + nome_arquivo)[0] + ".mp3"  # Troca a extensão para .mp3
        novo_arquivo = os.path.join(caminho_download, novo_nome)

# Renomeia o arquivo
        os.rename(arquivo_baixado, novo_arquivo)

        messagebox.showinfo("Sucesso", "Download do áudio em MP3 concluído!")
    else:
        messagebox.showerror("Erro", "Opção inválida. Por favor, escolha 'MP4' ou 'MP3'.")

# Placeholder
placeholder = "Cole seu link aqui"

# Função para remover placeholder ao clicar
def placeholderoff(event):
    if link_entry.get() == placeholder:
        link_entry.delete(0, tk.END)
        link_entry.config(fg="black")  # Muda a cor do texto para preto

# Função para restaurar placeholder se o campo estiver vazio
def placeholderon(event):
    if link_entry.get() == "":  # Verifica se o campo está vazio
        link_entry.insert(0, placeholder)
        link_entry.config(fg="gray")  # Mantém o placeholder cinza

# Criando a janela principal
root = tk.Tk()
root.title("𓅔 Alexsander Lucio Youtube Downloader 𓅔")

# Tamanho da janela
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Título principal
titulo = tk.Label(root, text="Youtube Downloader", font=("Rockwell", 30, "bold"), fg="Red")
titulo.pack(pady=20)

# Campo de entrada para o link do vídeo
tk.Label(root, text="Copie link do vídeo que deseja baixar:", font=("Rockwell", 12, "bold"), bg="#f0f0f0").pack(pady=20)

# Caixa de entrada do link com placeholder dinâmico
link_entry = tk.Entry(root, width=45, font=("Rockwell", 14, "italic"), bd=2, relief="solid", highlightthickness=2,
                      highlightcolor="#FF5733", fg="gray", justify= "center")  # Placeholder começa cinza
link_entry.insert(0, placeholder)  # Insere o placeholder ao iniciar
link_entry.bind("<FocusIn>", placeholderoff)
link_entry.bind("<FocusOut>", placeholderon)
link_entry.pack()

# Opções de escolha entre MP4 e MP3 lado a lado
escolha_var = tk.StringVar(value="MP4")
frame_opcoes = tk.Frame(root, bg="#f0f0f0")
frame_opcoes.pack(pady=20)

# Estilo para os botões de seleção
botao_discreto = {
    "font": ("comic sans", 12, "bold"),
    "fg": "#333",
    "bd": 0,
    "width": 6,
    "height": 2,
    "activebackground": "red",
    "activeforeground": "white"
}

# Botões de MP4 e MP3
mp4_button = tk.Radiobutton(frame_opcoes, text="MP4", variable=escolha_var, value="MP4", **botao_discreto)
mp4_button.pack(side=tk.LEFT, padx=20)

mp3_button = tk.Radiobutton(frame_opcoes, text="MP3", variable=escolha_var, value="MP3", **botao_discreto)
mp3_button.pack(side=tk.LEFT, padx=20)

# Botão para iniciar o download
download_button = tk.Button(root, text="Baixar", command=iniciar_download, font=("Arial", 14, "bold"), bg="Red",
                            fg="white", bd=0, relief="solid", padx=20, pady=10)
download_button.pack(pady=40)

# Inicia o loop da interface gráfica
root.mainloop()
