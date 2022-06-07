def euclides_estendido(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = euclides_estendido(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = euclides_estendido(a, m)
    if g != 1:
        print("Não existe inverso modular")
    else:
        return x % m

a = 137
m = 2887
print(modinv(a, m))
