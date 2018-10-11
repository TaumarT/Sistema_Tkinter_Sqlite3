# fornecedor.py
from tkinter import *
import sqlite3

janela = Tk()

janela.title("Sistema Loja")


def banco():
    nome = Nome_con.get()
    numero = Numero_con.get()
    produto = Produto_f.get()
    valor = Valor_prod.get()
    quantidade = Quantidade_prod.get()
    data = Data_compra_p.get()
    prazo = Prazo_compra.get()
   
  

    conn = sqlite3.connect('fornecedor.db')

    conn.execute('INSERT INTO fornecedor(nome, numero, produto, valor, quantidade, data, prazo) VALUES(?,?,?,?,?,?,?)', (nome, numero, produto, valor, quantidade, data, prazo))

    conn.commit()
    conn.close()




Nome_contato = Label(janela, text="Nome:")
Nome_contato.place(x=60, y=50)
Nome_con = Entry(janela)
Nome_con.place(x=100, y=50)

Numero_contato = Label(janela, text="Numero:")
Numero_contato.place(x=50, y=80)
Numero_con = Entry(janela)
Numero_con.place(x=100, y=80)

Produto = Label(janela, text="Produto:")
Produto.place(x=50, y=115)
Produto_f = Entry(janela)
Produto_f.place(x=100, y=115)

Valor_produto = Label(janela, text="Valor:")
Valor_produto.place(x=65, y=150)
Valor_prod = Entry(janela)
Valor_prod.place(x=100, y=150)

Quantidade_produto = Label(janela, text="Quantidade:")
Quantidade_produto.place(x=30, y=180)
Quantidade_prod = Entry(janela)
Quantidade_prod.place(x=100, y=180)

Data_compra = Label(janela, text="Data:")
Data_compra.place(x=70, y=210)
Data_compra_p = Entry(janela)
Data_compra_p.place(x=100, y=210)

Prazo_compra_produto = Label(janela, text="Prazo:")
Prazo_compra_produto.place(x=65, y=240)
Prazo_compra = Entry(janela)
Prazo_compra.place(x=100, y=240)




bt = Button(janela, text="confirmar", width=30, command= banco)
bt.place(x=90, y=380)

# ed1 = Entry(janela)
# ed1.place(x=100, y=100)


janela.geometry("450x700+50+50")
janela.mainloop()
