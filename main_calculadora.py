from tkinter import *
from tkinter import ttk

# =====================  ATUALIZANDO BRANCH RAQUEL IGUAL MAIN ===================== #

# ================================================================================ #

from tkinter import *   
from tkinter import ttk       

azul_escuro1 = "#010628"  
branco2 = "#FEFFFE"
laranja3 = "#FC4F0F" 
azulzinho4 = "#61A5FF" 
botao_laranja5 = "#FFAB40" 
bot_rosa6 = "#F603ED"
bot_rosafundo = "#A957C0" 
bot_rosaescuro8 = "#B0077D" 
bot_rosaclara9 = "#FBBBE7"
bot_rosinha10 = "#E9B8DA"

janela = Tk() 
janela.title("Calculadora - titulo") 
janela.geometry("235x326") 
janela.resizable(width= False, height= False) 
janela.config(bg='black')

frem_tela = Frame(janela, width=235, height=65, bg=bot_rosaescuro8)

frem_corpo = Frame(janela, width=235, height=268, bg=bot_rosaclara9)
frem_corpo.grid(row=1, column=0)            

todos_valores =''

valor_texto = StringVar()

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    #passando valor para tela
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))
    todos_valores = (str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


app_label = Label(frem_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, bg=bot_rosaescuro8, fg=branco2,  font=('Ivy 18 ')) # MUDEI A COR DO FUNDO PARA ROSA ESCURO para melhorar a visualização dos números (contraste) -> Liriel
app_label.place(x=0,y=0)

botao_1 = Button(frem_corpo, command=limpar_tela, text="C", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=0) 

botao_2 = Button(frem_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=118, y=0)

botao_3 = Button(frem_corpo, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=bot_rosa6, fg=branco2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=177, y=0)

botao_4 = Button(frem_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=0, y=52)

botao_5 = Button(frem_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=59, y=52)

botao_6 = Button(frem_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=118, y=52)

botao_7 = Button(frem_corpo, command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=bot_rosa6, fg=branco2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_7.place(x=177, y=52)

botao_8 = Button(frem_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_8.place(x=0, y=104)

botao_9 = Button(frem_corpo, command = lambda: entrar_valores('5'), text="5", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_9.place(x=59, y=104)

botao_10 = Button(frem_corpo, command = lambda: entrar_valores('6'), text="6", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_10.place(x=118, y=104)

botao_11 = Button(frem_corpo, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=bot_rosa6, fg=branco2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_11.place(x=177, y=104)

botao_12 = Button(frem_corpo, command = lambda:  entrar_valores('1'), text="1", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_12.place(x=0, y=156)

botao_13 = Button(frem_corpo, command = lambda: entrar_valores('2'), text="2", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_13.place(x=59, y=156)

botao_14 = Button(frem_corpo, command = lambda: entrar_valores('3'), text="3", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_14.place(x=118, y=156)

botao_15 = Button(frem_corpo, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=bot_rosa6, fg=branco2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_15.place(x=177, y=156)

botao_16 = Button(frem_corpo, command = lambda: entrar_valores('0'), text="0", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_16.place(x=0, y=208)

botao_17 = Button(frem_corpo, command = lambda: entrar_valores('.'), text=".", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_17.place(x=118, y=208)

botao_18 = Button(frem_corpo, command = calcular, text="=", width=5, height=2, bg=bot_rosa6, fg=branco2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_18.place(x=177, y=208)

janela.mainloop()

