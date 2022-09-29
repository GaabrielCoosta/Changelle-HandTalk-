"""
MIT License

Copyright (c) 2022 Gabriel Costa Andrade

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import cereja as cj
import time
from langdetect import detect
from Uteis import cabecalho

cabecalho('-- IDENTIFICADOR DE IDIOMAS --')
# Função disponível em __init__.py, retorna a formatação do cabeçalho

while True:
# Criei o 'while True', para que o usuário pudesse obter mais de um resultado
# Utilizei da função 'detect()' para obter o resultado esperado
# Utilizei a função 'cj.Progress.prog()' para deixar o código mais legal :)

    texto = str(input('Digite uma frase: '))
    idioma = detect(texto).upper()
    interagindo = texto.split()

    for i in cj.Progress.prog(interagindo):
        print(f"Analisando: {i}")
        time.sleep(2)

    print(f'\033[1:33mIDIOMA IDENTIFICADO >>\033[m {idioma}')
    print('=-='*20)

    p = str(input('Deseja continuar identificando idiomas? [S|N]: ')).strip().upper()
    while p not in 'NnSs':
        print('\033[1:31mErro de digitação!\033[m')
        p = str(input('Deseja continuar identificando idiomas: ')).strip().upper()

    if p == 'N':
        print('\033[1:34mObrigado, volte sempre!\033[m')
        break
