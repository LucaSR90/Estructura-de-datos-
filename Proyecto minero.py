# Datos: Matriz Binaria para representar la extracción de minerales (1: extraído, 0: no extraído)
minerales = ['Oro', 'Plata', 'Cobre', 'Hierro', 'Carbón']
minas = ['Mina A', 'Mina B', 'Mina C']

extraccion = [
    [1, 0, 0],  # Oro
    [0, 1, 0],  # Plata
    [1, 0, 0],  # Cobre
    [0, 1, 0],  # Hierro
    [1, 0, 0],  # Carbón
]

# Mostrar la matriz de extracción en consola
def mostrar_extraccion(matriz, minerales, minas):
    print("Matriz de Extracción de Minerales:")
    print(f"{'Mineral':<10} {'Mina A':<6} {'Mina B':<6} {'Mina C':<6}")
    for i, mineral in enumerate(minerales):
        fila = matriz[i]
        print(f"{mineral:<10} {fila[0]:<6} {fila[1]:<6} {fila[2]:<6}")

mostrar_extraccion(extraccion, minerales, minas)

# Simulación de predicción básica usando lógica condicional simple
# Predicción: si hay extracción en Mina A o Mina B, asumimos que también lo habrá en Mina C
def predecir_extraccion(nuevos_datos):
    predicciones = []
    for dato in nuevos_datos:
        # Regla simple: si hay extracción en Mina A o Mina B, predecimos que habrá extracción en Mina C
        if dato[0] == 1 or dato[1] == 1:
            predicciones.append(1)  # 'Sí' para extracción
        else:
            predicciones.append(0)  # 'No' para extracción
    return predicciones

# Nuevos escenarios para predecir
nuevos_datos = [
    [1, 0],  # Mina A extrae, Mina B no
    [0, 1],  # Mina A no extrae, Mina B sí
    [1, 1],  # Ambas extraen
    [0, 0],  # Ninguna extrae
]

predicciones = predecir_extraccion(nuevos_datos)

# Mostrar resultados de predicción
print("\nPredicción de Extracción de Minerales en Mina C:")
for i, dato in enumerate(nuevos_datos):
    print(f"Minerales extraídos en Mina A: {dato[0]}, Mina B: {dato[1]} -> Predicción para Mina C: {'Sí' if predicciones[i] == 1 else 'No'}")
