#consulta.py
from tkinter import *
import sqlite3

janela = Tk()
janela.title("Sistema Loja")




conn = sqlite3.connect('fornecedor.db')
c = conn.cursor()
def procurar():
	nome = cons.get()
	c.execute("SELECT nome FROM fornecedor")

	for fonc in c.fetchall():
		print(fonc)

	c.close()
	conn.close()



consulta = Label(janela, text="Consulta:")
consulta.place(x=100, y=180)
cons = Entry(janela)
cons.place(x=100, y=50)



#lista = Listbox(janela,width=100)
#lista.place(x=200, y=200)
#lista.insert(procurar())
#lista.pack()

bt = Button(janela, text="confirmar", width=30, command= procurar)
bt.place(x=30, y=50)


janela.geometry("700x300+200+50")
janela.mainloop()