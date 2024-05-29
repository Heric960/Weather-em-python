from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Cores
cor_1 = '#444466' #Preta
cor_2 = '#feffff' #Branca
cor_3 = '#6f9fbd' #Azul
fundo_dia = '#6cc4cc'
fundo_note = '#484f60'
fundo_tarde = '#bfb86d'

fundo = fundo_dia

# Janela
janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=159)

# Frame Top
frame_top = Frame(janela, width=320, height=50, bg=cor_2, pady=0, padx=0)
frame_top.grid(row=1,column=0)

# Frame body
frame_body = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_body.grid(row=2,column=0, stick=NW)

# Estilizando
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Campo de esntada
e_local = Entry(frame_top, width=20, justify='left', font=('', 14), highlightthickness=1, relief='solid')
e_local.place(x=14, y=10)

# Configurando o botão
b_local = Button(frame_top, text='Ver Clima', bg=cor_2, fg=cor_3,font=('Ivy 9 bold'), relief='raised', overrelief=RIDGE)
b_local.place(x=250, y=10)

# Campo de saida localidade (Cidade - Pais / Continente)
l_cidade = Label(frame_body, text='Umuarama - Brazil / South America', anchor='center',bg=fundo, fg=cor_2,font=('Arial 14'))
l_cidade.place(x=10, y=4)

# Campo de saida data/hora (dd/mm/aa | h:m:s)
l_data = Label(frame_body, text='29 05 2024 | 12:13:00 PM', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10'))
l_data.place(x=10, y=54)

# Campo de saida humidade relativa
l_humidade = Label(frame_body, text='84', anchor='center',bg=fundo, fg=cor_2,font=('Arial 45'))
l_humidade.place(x=10, y=100)

l_porcentagen = Label(frame_body, text='%', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10 bold'))
l_porcentagen.place(x=85, y=110)

l_humidade_p = Label(frame_body, text='Humidade', anchor='center',bg=fundo, fg=cor_2,font=('Arial 8'))
l_humidade_p.place(x=85, y=140)

# Campo de saida pressão
l_pressao = Label(frame_body, text='Pressão : 1000', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10'))
l_pressao.place(x=10, y=184)

# Campo de saida velocidade do vento
l_velocidade = Label(frame_body, text='Velocidade do vento : 1000', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10'))
l_velocidade.place(x=10, y=212)

# Campo de saida estado do clima
l_descircao = Label(frame_body, text='Nublado', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10'))
l_descircao.place(x=170, y=190)

# Adicionar a imagen sol dia
imagen = Image.open('imagens/sol_dia.png')
imagen = imagen.resize((130, 130))
imagen = ImageTk.PhotoImage(imagen)

l_Icon = Label(frame_body, image=imagen,bg=fundo)
l_Icon.place(x=160, y=50)

janela.mainloop()



