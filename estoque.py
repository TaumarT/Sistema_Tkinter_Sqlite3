# estoque.py
from tkinter import *
import sqlite3

janela = Tk()

janela.title("Sistema Loja")


def banco_estoque():

    cod = Cod.get()
    nome = Nome.get()
    preco = Preco.get()
    estoque = Estoque.get()
    
  

    conn = sqlite3.connect('estoque.db')

    conn.execute('INSERT INTO cadastro_produto(cod, nome, preco, estoque) VALUES(?,?,?,?)', (cod, nome, preco, estoque))
    conn.commit()
    conn.close()



Codigo = Label(janela, text="Codigo:")
Codigo.place(x=50, y=50)
Cod = Entry(janela)
Cod.place(x=100, y=50)

nome = Label(janela, text="Nome:")
nome.place(x=55, y=80)
Nome = Entry(janela)
Nome.place(x=100, y=80)

preco = Label(janela, text="Preço:")
preco.place(x=55, y=115)
Preco = Entry(janela)
Preco.place(x=100, y=115)

estoque = Label(janela, text="Nº estoque:")
estoque.place(x=30, y=150)
Estoque = Entry(janela)
Estoque.place(x=100, y=150)


bt = Button(janela, text="confirmar", width=30, command= banco_estoque)
bt.place(x=90, y=200)

# ed1 = Entry(janela)
# ed1.place(x=100, y=100)


janela.geometry("400x250+150+150")
janela.mainloop()