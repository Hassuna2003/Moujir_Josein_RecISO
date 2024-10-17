import random #Importamos la libreria random que nos permitirá generar números aleatorios

#Esta es la lista donde meteremos los números del usuario y los aleatorios
lista_numeros = []

numero = int(input("Introduce un número (-1 para dejar de introducir): "))

while numero != -1:
    lista_numeros.append(numero)
    numero = int(input("Introduce un número (-1 para dejar de introducir): "))

# Añadir 5 números aleatorios a la lista
for i in range(5):
    numero_aleatorio = random.randint(0,10)
    lista_numeros.append(numero_aleatorio)

#Mostramos la lista de la lista completa
print("Lista actual de números (incluyendo los números aleatorios): ", lista_numeros)

#Pedimos al usuario un número para ver cuántas veces aparece en la lista
numero_a_buscar = int(input("Introduce un número para ver cuántos números hay mayores que ese: "))

numeros_mayores = 0
for numero in lista_numeros:
    if numero > numero_a_buscar:
        numeros_mayores += 1

#Resultado de cuántas veces aparece en la lista el número:
print("Hay", numeros_mayores , "numeros mayores que" , numero_a_buscar)
