import random

def contar_intentos(valor_buscado):
    # Validación del rango permitido
    if not 2 <= valor_buscado <= 12:
        return "Error: el valor debe estar entre 2 y 12."
    
    intentos = 0
    
    while True:
        dado_a = random.randint(1, 6)
        dado_b = random.randint(1, 6)
        total = dado_a + dado_b
        intentos += 1
        
        if total == valor_buscado:
            break
            
    return intentos