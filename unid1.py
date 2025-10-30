# -*- coding: utf-8 -*-
import math
import sys
from symbol import return_stmt

# Exercício: Mostrar de dias para anos, meses e dias

IdadeNicholasEmDias = input("Digite sua idade em anos \n")
IdadeParaAno = IdadeNicholasEmDias / 365
IdadeParaMeses = IdadeNicholasEmDias % 365 / 30
IdadeParaDias = IdadeNicholasEmDias % 365 % 30
mesesoumes = " mês " if IdadeParaMeses == 1 else " meses "
print ("Tenho " + str(IdadeParaAno) + " anos, " + str(IdadeParaMeses) + mesesoumes + "e "
       + str(IdadeParaDias) + " dias")

# Exercício: Calcular área do triângulo

TrianguloA = float(input("Digite o valor da parte A do triangulo \n"))
TrianguloB = float(input("Digite o valor da parte B do triangulo \n"))
TrianguloC = float(input("Digite o valor da parte C do triangulo \n"))

if (TrianguloA + TrianguloB <= TrianguloC or
        TrianguloA + TrianguloC <= TrianguloB or
        TrianguloB + TrianguloC <= TrianguloA):
    print("Lados inválidos para existir um triângulo")

semiperimetro = (TrianguloA + TrianguloB + TrianguloC) / 2

if (semiperimetro <= TrianguloA or semiperimetro <= TrianguloB or semiperimetro <= TrianguloC):
    print ("Lados inválidos para existir um perimetro de triangulo")

Area = math.sqrt(
    semiperimetro * (semiperimetro - TrianguloA) * (semiperimetro - TrianguloB) * (semiperimetro - TrianguloC))

resultado = "Existe triangulo e sua área é " + str(round(Area, 2))

print (resultado)


# Exercício: Mostrar o menor de 3 números

def ler_inteiro(prompt):
    while True:
        entrada = input(prompt)
        try:
            numero = int(entrada)  # tenta converter para inteiro
            return numero
        except ValueError:
            print("Erro: digite um número inteiro válido.")


primeironumero = ler_inteiro("Digite o primeiro numero \n")
segundonumero = ler_inteiro("Digite o segundo numero \n")
terceironumero = ler_inteiro("Digite o terceiro numero \n")
menornumero = ""
if (primeironumero < segundonumero and primeironumero < terceironumero): menornumero = primeironumero
if (segundonumero < primeironumero and segundonumero < terceironumero): menornumero = segundonumero
if (terceironumero < segundonumero and terceironumero < primeironumero): menornumero = terceironumero

print("O menor número é o " + str(menornumero))


# Exercício listando números primos

def ler_inteiro():
    n = 101
    eprimo = True

    for i in range(1, n):
        w = i
        for j in range(1, w):
            if w % j == 0:
                eprimo = False
                break

            elif w % j > 0:
                eprimo = True

        if eprimo:
            print (str(i) + " é primo ")

        else:
            print(str(i) + " não é primo ")


ler_inteiro()


def inverter_letras(frase):
    # Divide a frase em palavras
    palavras = frase.split()
    print (palavras)

    # Inverte cada palavra
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    print (palavras_invertidas)

    # Junta as palavras de volta em uma frase
    nova_frase = " ".join(palavras_invertidas)

    return nova_frase


print ("Digite uma frase: \n")
frase = sys.stdin.readline()
resultado = inverter_letras(frase)
print(resultado)
