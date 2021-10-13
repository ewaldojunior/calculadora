from tkinter import *

janela = Tk()
janela.title("Calculadora")

def click_igual():
    segundo_numero = visor.get()
    visor.delete(0, END)
    if matematica == "soma":
        visor.insert(0, p_numero + float(segundo_numero))
    if matematica == "subtracao":
        visor.insert(0, p_numero - float(segundo_numero))
    if matematica == "multiplicacao":
        visor.insert(0, p_numero * float(segundo_numero))
    if matematica == "divisao":
        visor.insert(0, p_numero / float(segundo_numero))

def click_soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "soma"
    p_numero = float(primeiro_numero)
    visor.delete(0, END)

def click_sub():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "subtracao"
    p_numero = float(primeiro_numero)
    visor.delete(0, END)

def click_mult():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "multiplicacao"
    p_numero = float(primeiro_numero)
    visor.delete(0, END)

def click_div():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "divisao"
    p_numero = float(primeiro_numero)
    visor.delete(0, END)

def click_ponto():
    visor.insert(END, ".")

def deletar():
    visor.delete(0, END)

def click_button(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(numero))

lb1 = Label(janela, text="CALCULADORA", font=("verdana", 20, "bold"), pady=10)
lb1.pack()

visor = Entry(janela, bg="#edfff8", font=("verdana", 12))
visor.pack()

#fileira 1:
bt1 = Button(janela, text="1", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(1))
bt1.place(x=10, y=100)

bt2 = Button(janela, text="2", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(2))
bt2.place(x=10, y=155)

bt3 = Button(janela, text="3", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(3))
bt3.place(x=10, y=210)

bt0 = Button(janela, text="0", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(0))
bt0.place(x=10, y=265)

#fileira 2:
bt4 = Button(janela, text="4", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(4))
bt4.place(x=60, y=100)

bt5 = Button(janela, text="5", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(5))
bt5.place(x=60, y=155)

bt6 = Button(janela, text="6", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(6))
bt6.place(x=60, y=210)

btPonto = Button(janela, text=".", bg="#a2eddb", pady=12, padx=40, bd=4, command= click_ponto)
btPonto.place(x=60, y=267)

#fileira 3:
bt7 = Button(janela, text="7", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(7))
bt7.place(x=110, y=100)

bt8 = Button(janela, text="8", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(8))
bt8.place(x=110, y=155)

bt9 = Button(janela, text="9", bg="#a2eddb", pady=14, padx=14, bd=4, command= lambda: click_button(9))
bt9.place(x=110, y=210)

#fileira 4:
btSoma = Button(janela, text="+", bg="#a2eddb", pady=14, padx=14, bd=4, command=click_soma)
btSoma.place(x=160, y=100)

btSub = Button(janela, text="-", bg="#a2eddb", pady=13, padx=15.49, bd=4, command=click_sub)
btSub.place(x=160, y=155)

btMult = Button(janela, text="x", bg="#a2eddb", pady=13, padx=15.4, bd=4, command=click_mult)
btMult.place(x=160, y=210)

btDiv = Button(janela, text="/", bg="#a2eddb", pady=13, padx=15.4, bd=4, command=click_div)
btDiv.place(x=160, y=265)

#botao de limpar CE:
btCE = Button(janela, text="CE", bg="#4dd1a8", pady=95, padx=14, bd=4, command= deletar)
btCE.place(x=210, y=100)

#botao igual:
btIgual = Button(janela, text="=", bg="#4dd1a8", pady=14, padx=117, bd=4, command=click_igual)
btIgual.place(x=10, y=320)


janela.resizable(False, False)
janela.geometry("280x380")
janela.mainloop()