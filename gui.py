
from tkinter import *


janela = Tk()

def principal():    
    tela()
    janela.mainloop()
    
def exibicao():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("                                                                          Menu Principal")
    janela.config(background="#49A")
    janela.geometry("700x550")
    janela.maxsize(width=900, height= 700)
    img = PhotoImage(file="artist arsenal.png")
    label_imagem = Label(janela,image=img).pack()
    botoes()
    janela.mainloop()

    
def tela():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("                                                                          Menu Principal")
    janela.config(background="#49A")
    janela.geometry("700x550")
    janela.maxsize(width=900, height= 700)
    janela.mainloop()


def botoes():
  botaoCadastro = Button(janela,text="Cadastrar Artista", activebackground="blue",bg="lightblue",width=50)
  botaoCadastro.place(x=170,y=330)
  botaoListar = Button(janela,text="Listagem", activebackground="blue",bg="lightblue",width=50)
  botaoListar.place(x=170,y=370)
  botaoBuscar = Button(janela,text="Procurar", activebackground="blue",bg="lightblue",width=50)
  botaoBuscar.place(x=170,y=410)
  botaoSair = Button(janela,text="Sair", activebackground="blue",bg="lightblue",width=50)
  botaoSair.place(x=170,y=450)

exibicao()
    