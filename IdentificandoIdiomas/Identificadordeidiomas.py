import cereja as cj
import time
from langdetect import detect
from Uteis import cabecalho

cabecalho('-- IDENTIFICADOR DE IDIOMAS --')

while True:

    texto = str(input('Digite uma frase: '))
    idioma = detect(texto).upper()
    interagindo = texto.split()

    for i in cj.Progress.prog(interagindo):
        print(f"Analisando: {i}")
        time.sleep(2)

    print(f'\033[1:33mIDIOMA IDENTIFICADO >>\033[m {idioma}')
    print('=-='*20)

    p = str(input('Deseja continuar identificando idiomas: ')).strip().upper()
    while p not in 'NnSs':
        print('\033[1:31mErro de digitação!\033[m')
        p = str(input('Deseja continuar identificando idiomas: ')).strip().upper()

    if p == 'N':

        print('\033[1:34mObrigado, volte sempre!\033[m')
        break
