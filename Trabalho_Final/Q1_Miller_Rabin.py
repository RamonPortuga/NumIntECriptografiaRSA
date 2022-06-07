#Função dada em aula que realiza o teste de Miller_Rabin
def miller_rabin(num, b):
    b %= num
    if b <= 1:
        return False
    
    q = num - 1
    k = 0
    while q % 2 == 0:
        k += 1
        q //= 2
    r = pow(b, q, num)
    
    print("Num: ", num)
    
    if r == 1 or r == (num - 1):
        return False
    i = 0
    while True:
        r = pow(r, 2, num)
        print("R: ", r)
        i += 1
        if r == 1:
            return True
        if i == k:
            return True
        #Abaixo, a condicional citada na resposta
        if r == (num - 1):
            return False

for n in range (5, 10):
    num = pow(2, pow(2, n)) + 1
    b = 2
    print(miller_rabin(num, b))
