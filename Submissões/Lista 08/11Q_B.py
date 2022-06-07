def pseudoprimos (base, limite):
    #Gera a lista de primos até 317
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
            131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
            197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
            271, 277, 281, 283, 293, 307, 311, 313, 317]
    lista = []
    lista_aux = []
    qtd_d = 0
    for i in range (2, limite + 1):
        if (pow (base, i, i) == pow (base, 1, i)):
            for j in range (0, len(primos)):
                if ((i % primos[j] == 0) and (i != primos[j])):
                    qtd_d += 1
                    break
            if (qtd_d == 1):
                lista.append (i)
            qtd_d = 0
    print (len(lista))

base = 2
limite = 100000
pseudoprimos (base, limite)
base = 7
limite = 100000
pseudoprimos (base, limite)

"""
Como Funciona: O programa se baseia em uma lista pré-definida (primos)
que tem em seu conteudo, todos os números primos até 317. Com isso,
ele realiza a lógica e retorna uma lista contendo todos os pseudoprimos
encontrados.
Por que Funciona: O programa realiza o Pequeno Teorema de Fermat
(na 1° Forma), caso o número analisado se encaixe dentro do teorema
proposto, ele será analisado novamente para checar se ele é primo.
Caso não seja, ele será armazenado dentro de uma lista (lista).
Com isso, o meu programa irá retornar todos os pseudoprimos no
intervalo dado.
"""

