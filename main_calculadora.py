from tkinter import *
from tkinter import ttk

#oie :)
# iniciando a calculadora simples rosa - LiriRack-atividade/main_calculadora.py - v1.0 - multiplicação e divisão
from tkinter import *   
from tkinter import ttk       

#cores
azul_escuro1 = "#010628"  #azul escuro
branco2 = "#FEFFFE"  # branco
laranja3 = "#FC4F0F" #laranja 
azulzinho4 = "#61A5FF" #azulzinho fundo
botao_laranja5 = "#FFAB40" #laranjain botões com os calculos
bot_rosa6 = "#F603ED"
bot_rosafundo = "#A957C0" # pa n°
bot_rosaescuro8 = "#B0077D" # fundo
bot_rosaclara9 = "#FBBBE7" #fundo
bot_rosinha10 = "#E9B8DA"

janela = Tk() 
janela.title("Calculadora - titulo") # titulo da janela
janela.geometry("235x326") # tamanho da janela
janela.resizable(width= False, height= False) #ele restringe que vc tente abrir mais do que a tela existe
janela.config(bg='black') # cor de fundo da janela

#  bg: background - fundo fg: foreground
# #criando frames
frem_tela = Frame(janela, width=235, height=65, bg=bot_rosinha10)
frem_tela.grid(row=0, column=0)                 #row=fileira, linha colunm= coluna #gri &  #color picker


frem_corpo = Frame(janela, width=235, height=268, bg=bot_rosaclara9)
frem_corpo.grid(row=1, column=0)                 #row=fileira, linha colunm= coluna #gri &  #color picker




janela.mainloop()
