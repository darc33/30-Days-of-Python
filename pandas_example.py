import imp
import pandas as pd
import numpy as np
import re

df = pd.read_csv('hacker_news.csv')

#Primeras cinco lineas

print('Las primeras cinco lineas son:\n', df.head(), '\n')

#Ultimas cinco lineas

print('Las ultimas cinco lineas son \n', df.tail(),'\n')

title_column = df['title']

print('Los titulos son:\n', title_column, '\n')

print(f'El archivo tiene {df.shape[0]} filas y {df.shape[1]} columnas\n')

regex_patern1 = r'Python'#r'[Pp]ython'
regex_patern2 = r'JavaScript'#r'[Jj]ava[Ss]ript'

matches = title_column[title_column.str.contains(regex_patern1, case=False)]

print(f'Se encontraron las siguientes coincidencias para {regex_patern1}:\n',matches,'\n')

matches = title_column[title_column.str.contains(regex_patern2, case=False)]

print(f'Se encontraron las siguientes coincidencias para {regex_patern2}:\n', matches)
