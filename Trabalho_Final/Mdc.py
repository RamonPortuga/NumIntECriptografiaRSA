# -*- coding: utf-8 -*-

#
# Função que calcula o MDC entre dois números
#
def algoritmo_euclides(a, b):
    dividendo, divisor = a, b
    resto = dividendo % divisor 
    while resto != 0:
        dividendo, divisor = divisor, resto
        resto = dividendo % divisor
    return divisor


#
# Testes
#
num1 = 323334641051581231397618509539503
num2 = 375540174683800065068030299201351
num3 = 422659682638742744115773545689701
print(algoritmo_euclides(num1, num3))
print(algoritmo_euclides(num1, num3) / num1) 
