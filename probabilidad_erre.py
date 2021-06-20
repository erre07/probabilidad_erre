
import random
import time

RED= '\033[31m'
GREEN = '\033[32m'
RESET = '\033[39m'
print("Yo soy ERRE y realice este programa para plasmar como se comportan las probabilidades")
print()
probTest = int(input("Probabilidad a testear : "))
print()
probTotal = int(input("Ingresa la probabilidad limite, en la mayoria de las situaciones se introduce un 100:  "))
print()
velocidadTest = float(input("Introduce el intervalo deseado entre cada intento en formato decimal: "))
print()
cicloAdentro = 0
cicloAfuera = 0
probRestante = probTotal - probTest
factorProbable = random.randint(1, probTotal)
#    sistema de salida

while True:
    factorProbable = random.randint(1, probTotal)
    if factorProbable  >= probRestante:
        resultado = True
        cicloAdentro += 1
    else:
        resultado = False
        cicloAfuera += 1
    if resultado == True: 
        print(GREEN +(f" Acierto numero {cicloAdentro}") + RESET)
    else:
            print(RED +  (f' Desacierto numero {cicloAfuera}') + RESET)
    time.sleep(velocidadTest)
    

