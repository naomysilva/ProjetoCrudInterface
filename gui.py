from tkinter import *
def dados():
    if Nome.get()=="" or Cpf.get() == "" or Matricula.get() == "" or Data.get() == "":
        x = Label (interface , text="Dados Não Enviados" , background="Red",width=20).place(x=200 , y=200)

    else:
        x = Label(interface,text="Dados Enviados",background="green",width=20).place(x=200,y=200)
        with open("nomes.txt","a",encoding="utf-8") as file:
            file.write(f"Nome do album: {Nome.get()} nome do artista: {Cpf.get()} Data de lancamento do album: {Matricula.get()} ultimo album lançado: {Data.get()}\n")
        Nome.delete(0,END)
        Cpf.delete(0,END)
        Matricula.delete(0,END)
        Data.delete(0,END)
def destruir():
    interface.destroy()

interface = Tk()
interface.title("Dados Usuario")
interface.geometry("500x600")
interface.configure(background='Black')
Label(interface,text="Nome do album:",background="white").pack(anchor=W)
Nome=Entry(interface)
Nome.pack(anchor=W)
Label(interface,text="Nome do artista:",background="white").pack(anchor=W)
Cpf=Entry(interface)
Cpf.pack(anchor=W)

Label(interface,text="Data de lancamento do album:",background="white").pack(anchor=W)
Matricula=Entry(interface)
Matricula.pack(anchor=W)
Label(interface,text="foi o ultimo album lançado?",background="white").pack(anchor=W)
Data=Entry(interface)
Data.pack(anchor=W)
botao = Button(interface,text="Enviar Dados", command=dados)
botao.place(x=0,y=160)
botao1 = Button(interface,text="Mostrar Dados", command=destruir)
botao1.place (x=0,y=200)
interface.mainloop()
interface1 = Tk()
interface1.title("Dados Sistema")
interface1.geometry("1000x600")
interface1.configure(background='Black')
with open("nomes.txt","r",encoding="utf-8") as file:
    for x in file.readlines():
        Label (interface1 , text=f"{x}" , background="white").pack (anchor=W)

interface1.mainloop()