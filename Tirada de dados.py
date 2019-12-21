from random import randrange

status = 1
diccionario = {}
número_grande = 0
nombre_grande = ""

while status == 1:
    nombre = input("\n Escribe tu nombre: ")
    número = randrange(12)

    diccionario[nombre] = número

    if número > número_grande:
        número_grande = número
        nombre_grande = nombre
    
    print(nombre + ", has sacado un " + str(número) + "\n")
    status = int(input("Elige lo que quieras hacer \n 1.Tirar \n 2.Finalizar \n"))

print(" ")

for e in diccionario:
    print(e + " ha sacado un " + str(diccionario[e]))

print("\n El ganador es " + nombre_grande + " con un " + str(número_grande))