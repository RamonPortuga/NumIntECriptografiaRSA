def miller_rabin(n, b):
    """
    Retorna True se o teste de Miller--Rabin para n com base b **prova**
    que n é composto, False nos outros casos
    """
    b %= n
    print(b)
    if b <= 1:
        #Return 1
        return False
    q = n - 1
    k = 0
    while q % 2 == 0:
        k += 1
        q //= 2
  
    r = pow(b, q, n)
    if r == 1 or r == (n - 1):
        #Return 2
        return False

    i = 0
    while True:
        r = pow(r, 2, n)
        i += 1
        if r == 1:
            return True
        if i == k:
            return True
        if r == (n - 1):
            #Return 3
            return False



n = 6
b = 7
print(miller_rabin(n, b))
