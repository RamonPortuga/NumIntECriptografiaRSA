def qtd_num_alt_compostos(n):
    qtd_d = 1
    maior_qtd_d = 0
    qtd_num = 0
    for i in range (1, n + 1):
        #Coloquei esse metade_i pq o úníco divisor de i depois de sua
        #metade é o próprio i. Logo, iniciei o qtd_d com 1 ao invés de 0.
        #Com isso, ganho em eficência na execução do código.
        metade_i = int (i / 2)
        for j in range (1, metade_i + 1):
            if (i % j == 0):
                qtd_d += 1
        if (qtd_d > maior_qtd_d):
            maior_qtd_d = qtd_d
            qtd_num += 1
        qtd_d = 1
    print (qtd_num)

n = 5000
qtd_num_alt_compostos (n)

"""
Corretude: Como podemos notar pela sua saída, o programa consegue cumprir
o seu papel. Isso ocorre porque ele checa todos os números de 1 até (incluindo)
N e procura pelos seus divisores. Com isso, armazena a quantidade de divisores
em qtd_d e caso qtd_d seja maior que o maior_qtd_d (maior quantidade de divisores
já registrada), ele irá printar o número altamente composto.


Finitude: O programa não executa eternamente pq os limites de sua execução
se limitam às sequências finitas de 1 até (n + 1) e de 1 até (metade_i + 1)

"""
