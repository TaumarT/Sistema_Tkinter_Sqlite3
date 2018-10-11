# Cliente.py
from tkinter import *
import sqlite3

janela = Tk()

janela.title("Sistema Loja")


def banco():
    nome = Nome.get()
    bairro = Bairro.get()
    firma = Firma.get()
    endereco = Endereco.get()
    numero = Numero.get()
    cnpj = Cnpj.get()
    fone = Fone.get()
    celular = Celular.get()
    cidade = Cidade.get()
    cep = Cep.get()
    estado = Estado.get()
    inscricao = Inscricao_estadual.get()
    comprador = Comprador.get()
    data = Data.get()
  

    conn = sqlite3.connect('cliente.db')

    conn.execute('INSERT INTO cliente(nome, bairro, firma, endereco, numero, cnpj, fone, celular, cidade, cep, estado, inscricao, comprador, data) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (nome, bairro, firma, endereco, numero, cnpj, fone, celular, cidade, cep, estado, inscricao, comprador, data))

    conn.commit()
    conn.close()



# janela["background"] = "#808080"



nomel = Label(janela, text="Nome:")
nomel.place(x=60, y=50)
Nome = Entry(janela)
Nome.place(x=100, y=50)

bairrol = Label(janela, text="Bairro:")
bairrol.place(x=60, y=80)
Bairro = Entry(janela)
Bairro.place(x=100, y=80)

firmal = Label(janela, text="firma:")
firmal.place(x=60, y=115)
Firma = Entry(janela)
Firma.place(x=100, y=115)

enderecol = Label(janela, text="endereço:")
enderecol.place(x=40, y=150)
Endereco = Entry(janela)
Endereco.place(x=100, y=150)

numero1 = Label(janela, text="numero:")
numero1.place(x=45, y=180)
Numero = Entry(janela)
Numero.place(x=100, y=180)

cnpj1 = Label(janela, text="cnpj:")
cnpj1.place(x=65, y=210)
Cnpj = Entry(janela)
Cnpj.place(x=100, y=210)

fone1 = Label(janela, text="fone:")
fone1.place(x=65, y=240)
Fone = Entry(janela)
Fone.place(x=100, y=240)

celular1 = Label(janela, text="celular:")
celular1.place(x=55, y=270)
Celular = Entry(janela)
Celular.place(x=100, y=270)

cidade1 = Label(janela, text="cidade:")
cidade1.place(x=55, y=300)
Cidade = Entry(janela)
Cidade.place(x=100, y=300)

cep1 = Label(janela, text="CEP:")
cep1.place(x=70, y=330)
Cep = Entry(janela)
Cep.place(x=100, y=330)

estado1 = Label(janela, text="estado:")
estado1.place(x=50, y=360)
Estado = Entry(janela)
Estado.place(x=100, y=360)

inscricao1 = Label(janela, text="inscrição estadual:")
inscricao1.place(x=45, y=390)
Inscricao_estadual = Entry(janela)
Inscricao_estadual.place(x=150, y=390)

comprador1 = Label(janela, text="comprador:")
comprador1.place(x=40, y=430)
Comprador = Entry(janela)
Comprador.place(x=110, y=430)

data_emissao1 = Label(janela, text="data emissão:")
data_emissao1.place(x=40, y=460)
Data = Entry(janela)
Data.place(x=120, y=460)



bt = Button(janela, text="confirmar", width=30, command= banco)
bt.place(x=90, y=580)

# ed1 = Entry(janela)
# ed1.place(x=100, y=100)


janela.geometry("450x500+50+50")
janela.mainloop()
