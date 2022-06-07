def gera_primos(n):
    r = [True] * n
    r[0] = r[1] = False
    p = []
    for i in range(int(n**0.5+1)):
        if r[i]:
            for j in range(i+i, n, i):
                r[j] = False
    return r

def pseudoprimos (base, limite):
    primos = gera_primos (limite)
    lista = []
    for i in range (2, limite + 1):
        result = pow (base, i - 1, i) 
        if (result == 1):
            if (not primos [i]):
                lista.append (i)
    print (lista)

base = int (input("Entre com a base: "))
limite = int (input ("Entre com o limite: "))
pseudoprimos (base, limite)

"""
Como Funciona: 
"""
