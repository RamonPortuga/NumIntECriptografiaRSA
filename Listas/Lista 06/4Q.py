import math as m
def primos_k_gemeos (k, limite):
    qtd_d = 2
    qtd_d_gemeo = 2
    par_gemeos = []
    lista_gemeos =[]
    for i in range (2, limite):
        raiz = int (m.sqrt(i))
        for j in range (2, raiz + 1):
            if (i % j == 0):
                qtd_d += 1
                break
        if (qtd_d == 2):
            gemeo = i + k
            raiz_g = int (m.sqrt(gemeo))
            for n in range (2, raiz_g + 1):
                if (gemeo % n == 0):
                    qtd_d_gemeo += 1
                    break
            if (qtd_d_gemeo == 2):
                par_gemeos.append (i)
                par_gemeos.append (gemeo)
                lista_gemeos.append(par_gemeos)
            par_gemeos = []
            qtd_d_gemeo = 2
        qtd_d = 2
    print (lista_gemeos)

k = int(input("Entre com um número K: "))
limite = int(input("Entre com o limite: "))
primos_k_gemeos (k, limite)


"""
Como Funciona: Para achar os números primos, o meu programa trabalha
com a lógica de achar números compostos, isto é, caso um número tenha
um fator maior ou igual a 2 e menor ou igual a sua raiz quadrada, ele
será composto. Caso não, ele será um número Primo.

Por que Funciona: Como dito, caso o programa não ache nenhum fator de
N, ele será primo. Caso sim, ele irá calcular o valor do seu suposto
gêmeo e checar se o mesmo também é primo. Se for, os dois números
primos serão armazenados em uma lista (par_gemeos) e, logo depois,
essa lista será armazenada em outra lista (lista_gemeos). Isso ocorre
para economizar o tempo de execução, já que seria menos custoso do que
printar cada par de gemêos.
"""
