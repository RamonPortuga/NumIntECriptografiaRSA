def pseudoprimos (base, limite):
    #Gera a lista de primos até 317
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
            131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
            197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
            271, 277, 281, 283, 293, 307, 311, 313, 317]
    lista = []
    qtd_d = 0
    for i in range (2, limite + 1):
        result = pow (base, i, i) 
        if (result == base):
            for j in range (0, len(primos)):
                if ((i % primos[j] == 0) and (i != primos[j])):
                    qtd_d += 1
                    break
            if (qtd_d == 1):
                lista.append (i)
            qtd_d = 0
    print (lista)

base = int (input("Entre com a base: "))
limite = int (input ("Entre com o limite: "))
pseudoprimos (base, limite)
