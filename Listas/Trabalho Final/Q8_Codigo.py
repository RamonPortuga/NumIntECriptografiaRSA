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

def junta_blocos(texto_blocos):
    texto_junto = ''.join(str(texto_blocos))
    return texto_junto

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


def descriptar (blocos, n, d):
    blocos = pow(blocos, d, n)
    txt_resultante = junta_blocos(blocos)
    txt_descriptado = desconverte_texto(txt_resultante)
    return txt_descriptado


phi = 6160
n = 6319
e = 4107
mensagem = 2823
d = euclides_estendido(e, phi)
d += phi
print(descriptar(mensagem, n, d))
mensagem = 2688
print(descriptar(mensagem, n, d))
mensagem = 398
print(descriptar(mensagem, n, d))
mensagem = 4335
print(descriptar(mensagem, n, d))
mensagem = 2273
print(descriptar(mensagem, n, d))
