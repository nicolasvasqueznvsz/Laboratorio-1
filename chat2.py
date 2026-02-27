# Solicitar datos al usuario
nombre = input("Ingrese el nombre del jugador: ")
num_lanzamientos = int(input("Ingrese el número de lanzamientos: "))

# Generar los lanzamientos aleatorios y guardarlos en una lista
lanzamientos = [random.randint(1, 6) for _ in range(num_lanzamientos)]

# Calcular porcentajes directamente
porc_presadas = (sum(1 for x in lanzamientos if x in [3, 4]) / num_lanzamientos) * 100
porc_cinco_seis = (sum(1 for x in lanzamientos if x in [5, 6]) / num_lanzamientos) * 100
porc_pate_perro = (sum(1 for x in lanzamientos if x in [1, 2]) / num_lanzamientos) * 100

# Mostrar resultados
print(f"\nJugador: {nombre}")
print("Lanzamientos:", lanzamientos)
print(f"\nResultados:")
print(f"Presadas (3-4): {porc_presadas:.2f}%")
print(f"5-6: {porc_cinco_seis:.2f}%")
print(f"Pate-perro (1-2): {porc_pate_perro:.2f}%")