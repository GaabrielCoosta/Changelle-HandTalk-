from itertools import chain, combinations

def slicingobject(ht):
    '''Retorna uma versão segmentável dos ht iteráveis. '''
    try:
        ht[:0]
        return ht
    except TypeError:
        return tuple(ht)

def partition(iterable):
    '''Retorna a lógica de particionamento '''
    s = slicingobject(iterable)
    n = len(s)
    b, mid, e = [0], list(range(1, n)), [n]

    splits = (d for i in range(n) for d in combinations(mid, i))
    return [[s[sl] for sl in map(slice, chain(b, d), chain(d, e))]
            for d in splits]

if __name__ == '__main__':
    s =str(input('Frase: '))
    s = s.split()
    for i in partition(s):
        print(list(map(lambda values: ' '.join(values), i)))
