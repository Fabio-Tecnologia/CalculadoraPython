
from tkinter import *
from tkinter import ttk

#CORES
cor1 = '#1d241f'  #PRETO
cor2 = '#ffffff'  #BRANCO
cor3 = '#171414'  #PRETO 02
cor4 = '#a39f9b'  #CINZA
cor5 = '#734e32'  #LARANJA ESCURO



#CORPO(FUNDO) DA CALCULADORA
janela = Tk()
janela.title("Calculadora")
janela.geometry("232x340") #Largura e Cumprimento
janela.config(bg=cor1)


#BORDA SUPERIOR DA TELA DA CALCULADORA(RESULTADO)
frame_tela = Frame(janela, width=233, height=60, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=233, height=440)
frame_corpo.grid(row=1, column=0)


#VARIAVEL GLOBAL TODOS_VALORES
todos_valores = ''

#CRIANDO LABEL
texto = StringVar()

#CRIANDO FUNÇÃO DA CALCULADORA
def valores(evento):

    global todos_valores

    todos_valores = todos_valores + str(evento)


    
    #passando o valor para a tela
    texto.set(todos_valores)


#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    texto.set(str(resultado))


#função limpa tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    texto.set('')









app_label = Label(frame_tela, textvariable=texto, width=16, height=2, padx=7,relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 17'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#CRIAÇÃO DOS BOTÕES
b1 = Button(frame_corpo, command=limpar_tela, text='C', width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=-8, y=0) #Movimentar os botões:  X horizontal e o Y vertical 
b2 = Button(frame_corpo, command= lambda: valores('%'), text='%', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=103, y=0)
b3 = Button(frame_corpo, command= lambda: valores('/'), text='/', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=155, y=0)

b4 = Button(frame_corpo, command= lambda: valores('7'), text='7', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=57)
b5 = Button(frame_corpo, command= lambda: valores('8'), text='8', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=51, y=57)
b6 = Button(frame_corpo, command= lambda: valores('9'), text='9', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=103, y=57)
b7 = Button(frame_corpo, command= lambda: valores('*'), text='*', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=155, y=57)

b8 = Button(frame_corpo, command= lambda: valores('4'), text='4', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=110)
b9 = Button(frame_corpo, command= lambda: valores('5'), text='5', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=51, y=110)
b10 = Button(frame_corpo, command= lambda: valores('6'), text='6', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=103, y=110)
b11 = Button(frame_corpo, command= lambda: valores('-'), text='-', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=155, y=110)

b12 = Button(frame_corpo, command= lambda: valores('1'), text='1', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=165)
b13 = Button(frame_corpo, command= lambda: valores('2'), text='2', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=51, y=165)
b14 = Button(frame_corpo, command= lambda: valores('3'), text='3', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=103, y=165)
b15 = Button(frame_corpo, command= lambda: valores('+'), text='+', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=155, y=165)

b16 = Button(frame_corpo, command= lambda: valores('0'), text='0', width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=-8, y=221) 
b17 = Button(frame_corpo, command= lambda: valores('.'), text='.', width=2, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=103, y=221)
b18 = Button(frame_corpo, command= calcular , text='=', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=155, y=221)







janela.mainloop() #PARA EXCUTAR A JANELA DA CALCULADORA E MANTER




