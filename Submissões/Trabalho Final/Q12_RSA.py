from random import randint

#Abaixo, Dicionários contendo as tabelas de conversão e desconversão
códigos_para_símbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
235: '%', 236: '@', 237: ' ', 238: '\n'}

símbolos_para_códigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
'5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
'-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
'%': 235, '@': 236, ' ': 237, '\n': 238}

#--------------------------------------------------------------------------------

#Função que converte o texto original usando a tabela de conversão dada
def converte_texto (texto):
    txt_convertido = str(texto)
    for simb, cod in símbolos_para_códigos.items():
        txt_convertido = txt_convertido.replace(simb, str(cod))
    return txt_convertido

#Função que desconverte o texto convertido 
def desconverte_texto(texto):
  """Desconverte o texto convertido utilizando a função converte_texto()."""
  texto_desconvertido = str(texto)
  texto_desconvertido = texto_desconvertido.replace("[","")
  texto_desconvertido = texto_desconvertido.replace("]","")
  texto_desconvertido = texto_desconvertido.replace(",","")
  texto_desconvertido = texto_desconvertido.replace(" ","")
  texto_desconvertido = [texto_desconvertido[i:i+3] for i in range(0, len(texto_desconvertido), 3)]
  for iterator, value in enumerate(texto_desconvertido):
    for codigo, simbolo in códigos_para_símbolos.items():
      if(str(value) == str(codigo)):
        texto_desconvertido[iterator] = simbolo
        break

  texto_desconvertido = ''.join(texto_desconvertido)
  
  return texto_desconvertido
#--------------------------------------------------------------------------------

#Função auxiliar que serve para quebrar os blocos
def quebra_blocos(n, texto):
    texto = str(texto)
    texto_blocos = [texto[i:i+n] for i in range(0, len(texto), n)]
    return texto_blocos

#Função auxiliar que serve para juntar os blocos
def junta_blocos(texto_blocos):
    texto_junto = ''.join(str(texto_blocos))
    return texto_junto


#--------------------------------------------------------------------------------
#Função dada em aula que realiza o teste de Miller_Rabin
def miller_rabin(n, b):
    b %= n
    if b <= 1:
        return False
    q = n - 1
    k = 0
    while q % 2 == 0:
        k += 1
        q //= 2
    r = pow(b, q, n)
    if r == 1 or r == (n - 1):
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
            return False

#Função dada em aula que realiza o Algoritmo Estendido de Euclides
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
        x_ant, x_novo = x_novo, (x_ant - x_novo * quociente)
        y_ant, y_novo = y_novo, (y_ant - y_novo * quociente)
        dividendo, divisor = divisor, resto
    return x_ant

#Função que realiza o algoritmo de Euclides
def algoritmo_euclides(a, b):
    dividendo, divisor = a, b
    resto = dividendo % divisor 
    while resto != 0:
        dividendo, divisor = divisor, resto
        resto = dividendo % divisor
    return divisor

#--------------------------------------------------------------------------------
#Função responsável pela geração de números primos
def gera_primos(n):
    cont = 0
    while (cont <= 10):
        cont = 0
        p = randint(pow(10, n), pow(10, n + 2))
        if((p % 2) == 0):
            continue
        for i in range (1, 10 + 2):
            b = randint(1, p)
            if(not (miller_rabin(p, b))):
                cont += 1
    return p

#Função responsável pela geração das chaves do RSA.
def gera_chaves():
    #Gera os primos P e Q
    p = gera_primos(50)
    q = gera_primos(100)
    n = p * q

    phi = (p - 1) * (q - 1)
    e = 0
    i = 2
    #Calcula um numero e inversivel modulo phi
    while(e == 0):
      if(algoritmo_euclides(i, phi) == 1):
          e = i
      else:
        i += 1

    #Calcula o inverso d de e mod(phi)
    d = euclides_estendido(e, phi)
    d += phi

    #Calcula o inverso inv_p de p mod(q)
    inv_p = euclides_estendido(p, q)
    if(inv_p < 0):
      inv_p += q

    #Calcula o inverso inv_q de q mod(p)
    inv_q = euclides_estendido(q, p)
    if(inv_q < 0):
      inv_q += p

    #Calcula as formas reduzidas de d mod p - 1 e q - 1
    d_mod_p = pow(d, 1, p - 1)
    d_mod_q = pow(d, 1, q - 1)

    return n, e, d, p, q, inv_p, inv_q, d_mod_p, d_mod_q
    
#--------------------------------------------------------------------------------

"""
Função responsável por encriptar o texto já convertido
usando as chaves publicas criadas.
"""

def encriptar(texto, n, e):
    txt_convertido = converte_texto(texto)
    txt_blocos = quebra_blocos(len(str(n)) - 1, txt_convertido)
    for key, value in enumerate (txt_blocos):
        txt_blocos[key] = str(pow(int(value), e, n))
    return txt_blocos

"""
Função responsável por descriptar o texto
usando as chaves publicas criadas.
"""
def descriptar (blocos, n, d):
    for key, value in enumerate(blocos):
        blocos[key] = pow(int(value), d, n)
    txt_resultante = junta_blocos(blocos)
    txt_descriptado = desconverte_texto(txt_resultante)
    return txt_descriptado

"""
Função responsável por descriptar o texto de maneira rápida
(usando o TCR) usando os parâmetros gerados na função
gera_chaves()
"""
def descriptar_rapido(texto, n, d, p, q, inv_p, inv_q, d_mod_p, d_mod_q):
    for key, value in enumerate(texto):
        texto[key] = (pow(int(value), d_mod_p, p) * q * inv_q) + (pow(int(value), d_mod_q, q) * p * inv_p)
        texto[key] = pow(texto[key], 1, n)
    texto_reunido = junta_blocos(texto)
    texto_descriptado = desconverte_texto(texto_reunido)
    return texto_descriptado

#--------------------------------------------------------------------------------

#Aqui começa o Main
texto = str(input("Entre com o texto que deseja que seja convertido e desconvertido: "))
n, e, d, p, q, inv_p, inv_q, d_mod_p, d_mod_q = gera_chaves()
print("\nIniciando o processo")
print("Usando a descriptação padrão:")
print(descriptar(encriptar(texto, n, e), n, d))
print("\nAgora, usando a descriptação rápida:")
print(descriptar_rapido(encriptar(texto, n, e), n, d, p, q, inv_p, inv_q, d_mod_p, d_mod_q))
print("\nFIM")
