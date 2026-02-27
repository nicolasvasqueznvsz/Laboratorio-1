import random

# 1. Solicitar el nombre del jugador
nombre = input("Por favor, introduce tu nombre: ")

# 2. Simular el lanzamiento de los dos dados
# Usamos random.randint(1, 6) para obtener un número entre 1 y 6
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print(f"\n{nombre} lanzó los dados y obtuvo: {dado1} y {dado2}")

# 3. Validar si obtuvo "presadas" (ambos dados iguales)
if dado1 == dado2:
    print(f"Felicitaciones {nombre}. Puedes sacar una ficha.")
else:
    print("Turno del siguiente jugador.")