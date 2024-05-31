from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc

# Cores
cor_1 = '#444466' #Preta
cor_2 = '#feffff' #Branca
cor_3 = '#6f9fbd' #Azul
fundo_dia = '#6cc4cc'
fundo_noite = '#484f60'
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

global imagen

# Função que retorna as informações
def informacoes():
    # Chave e link da Api
    CHAVE = '2ae18c6febbe6b99dd9118492bf32124'
    cidade = e_local.get()
    API_LINK = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={CHAVE}'

    # Fazendo a chamada da api usando o request
    rec = requests.get(API_LINK)

    # Convertendo os dados presentes na vairavel 'rec' em um dicionario
    dados = rec.json()

    # print(dados)

    # Obitendo zona, pais e hora
    pais_codigo = dados['sys']['country']
    # zona
    zona_fuso = pytz.country_timezones[pais_codigo]
    # Pais
    pais = pytz.country_names[pais_codigo]

    # Data
    time_zone = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(time_zone)
    zona_horas = zona_horas.strftime('%d %m %y | %H:%M:%S %p')

    # Tempo
    tempo = dados['main']['temp']
    pressao = dados['main']['pressure']
    humidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']

    # Mudando informações
    def pais_para_continete(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
        return pais_continente_nome

    continete = pais_para_continete(pais)

    # Passando as informaçoes
    l_cidade['text'] = cidade + " - "+ pais + " / " + continete
    l_data['text'] = zona_horas
    l_humidade['text'] = humidade
    l_pressao['text'] = 'Pressão do ar :' + str(pressao)
    l_velocidade['text'] = 'Velocidade do vento :' + str(velocidade)
    l_humidade_p['text'] = 'Humidade'
    l_porcentagen['text'] = '%'
    l_descircao['text'] = descricao

    # Logica para trocar o periodo
    zona_periodo = datetime.now(time_zone)
    zona_periodo = zona_periodo.strftime("%H")

    global imagen

    zona_periodo = int(zona_periodo)

    if zona_periodo <= 5:
        imagen = Image.open('imagens/lua.png')
        fundo = fundo_noite
    elif zona_periodo <= 11:
        imagen = Image.open('imagens/sol_dia.png')
        fundo = fundo_dia
    elif zona_periodo <= 17:
        imagen = Image.open('imagens/sol.png')
        fundo = fundo_tarde
    elif zona_periodo <= 23:
        imagen = Image.open('imagens/lua.png')
        fundo = fundo_noite
    else:
        pass

    imagen = imagen.resize((130, 130))
    imagen = ImageTk.PhotoImage(imagen)
    l_Icon = Label(frame_body, image=imagen, bg=fundo)
    l_Icon.place(x=160, y=50)

    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_body.configure(bg=fundo)

    l_cidade['bg'] = fundo
    l_data['bg'] = fundo
    l_humidade['bg'] = fundo
    l_pressao['bg'] = fundo
    l_velocidade['bg'] = fundo
    l_humidade_p['bg'] = fundo
    l_porcentagen['bg'] = fundo
    l_descircao['bg'] = fundo



# Campo de esntada
e_local = Entry(frame_top, width=20, justify='left', font=('', 14), highlightthickness=1, relief='solid')
e_local.place(x=14, y=10)

# Configurando o botão
b_local = Button(frame_top, command=informacoes, text='Ver Clima', bg=cor_2, fg=cor_3,font=('Ivy 9 bold'), relief='raised', overrelief=RIDGE)
b_local.place(x=250, y=10)

# Campo de saida localidade (Cidade - Pais / Continente)
l_cidade = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_2,font=('Arial 14'))
l_cidade.place(x=10, y=4)

# Campo de saida data/hora (dd/mm/aa | h:m:s)
l_data = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10'))
l_data.place(x=10, y=54)

# Campo de saida humidade relativa
l_humidade = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_2,font=('Arial 45'))
l_humidade.place(x=10, y=100)

l_porcentagen = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10 bold'))
l_porcentagen.place(x=85, y=110)

l_humidade_p = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_2,font=('Arial 8'))
l_humidade_p.place(x=85, y=140)

# Campo de saida pressão
l_pressao = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10'))
l_pressao.place(x=10, y=184)

# Campo de saida velocidade do vento
l_velocidade = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10'))
l_velocidade.place(x=10, y=212)

# Campo de saida estado do clima
l_descircao = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_2,font=('Arial 10'))
l_descircao.place(x=170, y=190)

janela.mainloop()



