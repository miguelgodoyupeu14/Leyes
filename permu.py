import math

# Función para calcular permutaciones lineales
def permutaciones(n):
    return math.factorial(n)

# Función para calcular variaciones
def variaciones(n, r):
    return math.factorial(n) / math.factorial(n - r)

# Función para calcular combinaciones
def combinaciones(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# Función para calcular permutaciones con repeticiones
def permutaciones_con_repeticiones(n, r):
    return n ** r

# Función para calcular variaciones con repeticiones
def variaciones_con_repeticiones(n, r):
    return n ** r

# Función para calcular combinaciones con repeticiones
def combinaciones_con_repeticiones(n, r):
    return math.factorial(n + r - 1) / (math.factorial(r) * math.factorial(n - 1))

# Función para calcular permutaciones circulares
def permutaciones_circulares(n):
    if n <= 1:
        return 1
    return math.factorial(n - 1)

# Función para calcular permutaciones con elementos repetidos
def permutaciones_repetidos(n, repeticiones):
    denominador = 1
    for r in repeticiones:
        denominador *= math.factorial(r)
    
    return math.factorial(n) / denominador

# Menú interactivo
def menu():
    print("\nMenú de Cálculos Combinatorios:")
    print("1. Permutaciones P(n, r)")
    print("2. Variaciones V(n, r)")
    print("3. Combinaciones C(n, r)")
    print("4. Permutaciones con repeticiones P_repetición(n, r)")
    print("5. Variaciones con repeticiones V_repetición(n, r)")
    print("6. Combinaciones con repeticiones C_repetición(n, r)")
    print("7. Permutaciones circulares P_circular(n)")
    print("9. Permutaciones con elementos repetidos P_repetidos(n, repeticiones)")
    print("0. Salir")

# Bucle para el menú
while True:
    menu()
    opcion = input("Seleccione una opción (0-9): ")

    if opcion == "1":
        n = int(input("Ingrese el valor de n: "))
        print(f"Permutaciones P({n}) = {permutaciones(n)}")
    
    elif opcion == "2":
        n = int(input("Ingrese el valor de n: "))
        r = int(input("Ingrese el valor de r: "))
        print(f"Variaciones V({n}, {r}) = {variaciones(n, r)}")
    
    elif opcion == "3":
        n = int(input("Ingrese el valor de n: "))
        r = int(input("Ingrese el valor de r: "))
        print(f"Combinaciones C({n}, {r}) = {combinaciones(n, r)}")
    
    elif opcion == "4":
        n = int(input("Ingrese el valor de n: "))
        r = int(input("Ingrese el valor de r: "))
        print(f"Permutaciones con repeticiones P_repetición({n}, {r}) = {permutaciones_con_repeticiones(n, r)}")
    
    elif opcion == "5":
        n = int(input("Ingrese el valor de n: "))
        r = int(input("Ingrese el valor de r: "))
        print(f"Variaciones con repeticiones V_repetición({n}, {r}) = {variaciones_con_repeticiones(n, r)}")
    
    elif opcion == "6":
        n = int(input("Ingrese el valor de n: "))
        r = int(input("Ingrese el valor de r: "))
        print(f"Combinaciones con repeticiones C_repetición({n}, {r}) = {combinaciones_con_repeticiones(n, r)}")
    
    elif opcion == "7":
        n = int(input("Ingrese el valor de n: "))
        print(f"Permutaciones circulares P_circular({n}) = {permutaciones_circulares(n)}")
    
    elif opcion == "9":
        n = int(input("Ingrese el valor de n: "))
        repeticiones = list(map(int, input("Ingrese las repeticiones de cada letra separadas por espacio: ").split()))
        print(f"Permutaciones con elementos repetidos P_repetidos({n}, {repeticiones}) = {permutaciones_repetidos(n, repeticiones)}")
    
    elif opcion == "0":
        print("¡Gracias por usar el programa!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 0 y 9.")
