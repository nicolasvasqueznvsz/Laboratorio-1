import random
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    return dado1, dado2, suma
nombre = input("Ingresa tu nombre: ")
numero_veces = int(input("Ingrese el número de veces que desea lanzar los dados: "))
resultados = []
presadas = 0
cinco_seis = 0
pateperro = 0
for i in range(numero_veces):
    d1, d2, suma = lanzar_dados()
    resultados.append(suma)
    print(f"Lanzamiento {i+1}: {d1} + {d2} = {suma}")
    if suma >= 7:
        presadas += 1
    elif suma == 5 or suma == 6:
        cinco_seis += 1
    elif suma == 1 or suma == 2:
        pateperro += 1

porcentaje_presadas = (presadas / numero_veces) * 100
porcentaje_cinco_seis = (cinco_seis / numero_veces) * 100
porcentaje_pateperro = (pateperro / numero_veces) * 100

print("Resultados para", nombre)
print("Lista de resultados:", resultados)
print(f"Presadas: {porcentaje_presadas:}%")
print(f"5-6: {porcentaje_cinco_seis:.}%")
print(f"Pate-perro (1-2): {porcentaje_pateperro:}%")