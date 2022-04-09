
from tkinter import *


janela = Tk()
#funcao que será main e chamara as demais
def principal():    
    tela()
    janela.mainloop()
##primeira tela a ser exibida    
def exibicao():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("                                                                          Menu Principal")
    janela.config(background="v ")
    janela.geometry("700x550")
    janela.maxsize(width=900, height= 700)
    img = PhotoImage(file="artist arsenal.png")
    label_imagem = Label(janela,image=img).pack()
    botoes()
    janela.mainloop()

#tela de sera contruida quando usuario apertar em voltar  
def tela():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("                                                                          Menu Principal")
    janela.config(background="#49A")
    janela.geometry("700x550")
    janela.maxsize(width=900, height= 700)
    janela.mainloop()

#botoes e label
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
    