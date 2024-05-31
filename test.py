import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc


# Chave e link da Api
CHAVE = '2ae18c6febbe6b99dd9118492bf32124'
cidade = 'São Paulo'
API_LINK = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={CHAVE}'

# Fazendo a chamada da api usando o request
rec = requests.get(API_LINK)

# Convertendo os dados presentes na vairavel 'rec' em um dicionario
dados = rec.json()

#print(dados)

# Obitendo zona, pais e hora
pais_codigo = dados['sys']['country']
# zona
zona_fuso = pytz.country_timezones[pais_codigo]
# Pais
pais = pytz.country_names[pais_codigo]

# Data
time_zone = pytz.timezone(zona_fuso[7])
zona_horas = datetime.now(time_zone)
zona_horas = zona_horas.strftime('%d %m %y | %H:%M:%S %p')

# Tempo
tempo = dados['main']['temp']
pressao = dados['main']['pressure']
humidade = dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']

# Mudando informações
#def pais_para_continete(i):
    #pais_alpha = pc.country_name_to_country_alpha2(i)
    #pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
    #pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
    #return pais_continente_nome

#continete = pais_para_continete(pais)

for i in zona_fuso:
    if dados['name'] == zona_fuso:
        print(zona_fuso[i])
