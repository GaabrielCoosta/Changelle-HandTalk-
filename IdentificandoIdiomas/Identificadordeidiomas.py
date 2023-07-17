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
from funcions import cabecalho

cabecalho('-- LANGUAGE IDENTIFIER --')
# Function available in __init__.py, returns header formatting


while True:
# I created the 'while True', so the user could get more than one result
# I used the 'detect()' function to get the expected result
# I used the 'cj.Progress.prog()' function to make the code nicer :)

    text = str(input('Type a sentence: '))
    leng = detect(text).upper()
    iterating = text.split()
    
    for i in cj.Progress.prog(iterating):
        print(
            f"Analyzing: {i}"
        )
        time.sleep(2)

    print(
        f'\033[1:33mLANGUAGE IDENTIFIED >>\033[m {leng}'
    )
    print('=-='*20)
    p = str(input(
        'Do you want to continue identifying languages? [Y|N]: ')
           ).strip().upper()
    
    
    while p not in 'NnSs':
        print(
            '\033[1:31m Writing error! \033[m'
        )
        p = str(input(
            'Do you want to continue identifying languages? [Y|N]: ')
               ).strip().upper()

        
    if p == 'N':
        print(
            '\033[1:34m Thank you! \033[m'
        )
        break
