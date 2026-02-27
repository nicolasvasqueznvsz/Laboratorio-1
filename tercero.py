import random
def Hasta_el_objetivo(objetivo):
    if objetivo < 2 or objetivo > 12:
        print("El numero debe estar entre 2 y 12.")
        return
    lanzamientos = 0
    while True:
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        lanzamientos += 1
        print(f"Lanzamiento {lanzamientos}: {dado_1} + {dado_2} = {dado_1 + dado_2}")
        if dado_1 + dado_2 == objetivo:
            print(f"se logro el objetitivo: ({objetivo})")
            print(f"Se usaron {lanzamientos} lanzamientos.")
            return lanzamientos
numero_objetivo=int(input("Ingrese un número entre 2 y 12: "))
Hasta_el_objetivo(numero_objetivo)