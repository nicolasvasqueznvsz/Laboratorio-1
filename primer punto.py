import random

def lanzar_dados():
    nombre=input("Ingrese su nombre:")
    dado1=random.randint(1, 6)
    dado2=random.randint(1, 6)
    print(f"lanzo los dados y como resultado tuvo: {dado1} y {dado2}")
    if dado1 == dado2:
        print(f"Felicitaciones {nombre} Puedes sacar una ficha")
    else:

        print(f"Turno del siguiente jugador")
