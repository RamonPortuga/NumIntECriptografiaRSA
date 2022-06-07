def euclides_estendido(p, q):
    """
    Como vimos em aula, o Algoritmo Estendido de Euclides nos serve
    para calcular o inverso modular
    """
    dividendo, divisor = p, q
    x_ant, y_ant = 1, 0
    x_novo, y_novo = 0, 1
    while divisor != 0:
        quociente, resto = divmod (dividendo, divisor)
        x_ant, x_novo = x_novo, (x_ant - x_novo*quociente)
        y_ant, y_novo = y_novo, (y_ant - y_novo*quociente)
        dividendo, divisor = divisor, resto
    return x_ant

n = 8989
p = 89
q = 101
e = 83
phi = (p - 1) * (q - 1)
d = euclides_estendido(e, phi)
d += phi
print(d)
