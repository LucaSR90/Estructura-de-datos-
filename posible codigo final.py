import pandas as pd
import random

# Crear una base de datos ficticia de minerales y extracciones
data = {
    'Mineral': ['Oro', 'Plata', 'Cobre', 'Hierro', 'Carbón'],
    'Cantidad Extraída (Toneladas)': [random.randint(100, 1000) for _ in range(5)],
    'Fecha de Extracción': pd.date_range(start='2023-01-01', periods=5, freq='M')
}
df = pd.DataFrame(data)

# Clase para implementar una cola usando dos pilas
class ColaConDosPilas:
    def __init__(self):
        self.pila1 = []
        self.pila2 = []

    def encolar(self, elemento):
        self.pila1.append(elemento)

    def desencolar(self):
        if not self.pila2:
            while self.pila1:
                self.pila2.append(self.pila1.pop())
        if not self.pila2:
            raise Exception("La cola está vacía")
        return self.pila2.pop()

    def esta_vacia(self):
        return not self.pila1 and not self.pila2

    def ver_cola(self):
        return self.pila1 + self.pila2[::-1]

# Crear una cola para manejar las solicitudes de extracción
solicitudes_extraccion = ColaConDosPilas()

# Funciones para el proyecto

def identificar_mineral(mineral):
    if mineral in df['Mineral'].values:
        return f"El mineral {mineral} está presente en la base de datos."
    else:
        return f"El mineral {mineral} no se encuentra en la base de datos."

def saber_cual_se_extrajo():
    return df[['Mineral', 'Cantidad Extraída (Toneladas)', 'Fecha de Extracción']]

def identificar_patrones_de_extraccion():
    patrones = df.groupby('Mineral').agg({'Cantidad Extraída (Toneladas)': 'sum'}).sort_values(by='Cantidad Extraída (Toneladas)', ascending=False)
    return patrones

def agregar_solicitud_extraccion(mineral, cantidad):
    solicitudes_extraccion.encolar({'Mineral': mineral, 'Cantidad': cantidad})
    return f"Solicitud de extracción de {cantidad} toneladas de {mineral} agregada a la cola."

def procesar_solicitud_extraccion():
    if solicitudes_extraccion.esta_vacia():
        return "No hay solicitudes de extracción en la cola."
    solicitud = solicitudes_extraccion.desencolar()
    return f"Procesando solicitud de extracción de {solicitud['Cantidad']} toneladas de {solicitud['Mineral']}."

def ver_solicitudes():
    cola = solicitudes_extraccion.ver_cola()
    if not cola:
        return "No hay solicitudes en la cola."
    return "Solicitudes en la cola: " + ", ".join([f"{solicitud['Cantidad']} toneladas de {solicitud['Mineral']}" for solicitud in cola])

# Arreglos unidimensionales y bidimensionales
minerales_unidimensional = ['Oro', 'Plata', 'Cobre', 'Hierro', 'Carbón']
produccion_bidimensional = [
    [random.randint(50, 150) for _ in range(5)],  # Producción de Oro en diferentes meses
    [random.randint(30, 100) for _ in range(5)],  # Producción de Plata en diferentes meses
    [random.randint(20, 80) for _ in range(5)],   # Producción de Cobre en diferentes meses
    [random.randint(40, 120) for _ in range(5)],  # Producción de Hierro en diferentes meses
    [random.randint(60, 200) for _ in range(5)]   # Producción de Carbón en diferentes meses
]

# Clase de datos para representar un mineral
class Mineral:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def __repr__(self):
        return f"Mineral(nombre={self.nombre}, cantidad={self.cantidad})"

# Ejemplo de uso de la clase Mineral
mineral_ejemplo = Mineral('Oro', 500)
print(f"\nEjemplo de registro de mineral: {mineral_ejemplo}")

# Matriz binaria para representar si un mineral ha sido extraído (1) o no (0)
matriz_binaria_extraccion = [
    [1 if random.random() > 0.5 else 0 for _ in range(5)] for _ in range(5)
]

print("\nMatriz binaria de extracción (1 = extraído, 0 = no extraído):")
for fila in matriz_binaria_extraccion:
    print(fila)

# Programa principal
while True:
    print("\nBase de datos de la minera:")
    print(df)

    # Identificar un mineral
    mineral_buscado = input("Ingrese el nombre del mineral que desea buscar (o 'salir' para terminar): ")
    if mineral_buscado.lower() == 'salir':
        break
    resultado_identificacion = identificar_mineral(mineral_buscado)
    print(resultado_identificacion)

    # Saber los minerales que se extrajeron
    df_extraccion = saber_cual_se_extrajo()
    print("\nMinerales extraídos:")
    print(df_extraccion)

    # Identificar patrones de extracción
    print("\nPatrones de extracción:")
    print(identificar_patrones_de_extraccion())

    # Agregar solicitudes de extracción personalizadas
    while True:
        mineral = input("Ingrese el nombre del mineral para la solicitud de extracción (o 'ver' para ver las solicitudes, 'procesar' para procesar solicitudes, 'salir' para terminar): ")
        if mineral.lower() == 'salir':
            break
        elif mineral.lower() == 'ver':
            print(ver_solicitudes())
        elif mineral.lower() == 'procesar':
            print("\nProcesando solicitudes de extracción:")
            while not solicitudes_extraccion.esta_vacia():
                print(procesar_solicitud_extraccion())
        else:
            cantidad = int(input(f"Ingrese la cantidad de {mineral} a extraer (en toneladas): "))
            print(agregar_solicitud_extraccion(mineral, cantidad))
