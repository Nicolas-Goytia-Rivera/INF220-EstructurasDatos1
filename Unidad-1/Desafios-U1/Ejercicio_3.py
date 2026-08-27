class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None # Este es nuestro 'puntero' al siguiente espacio en el Heap

# --- Prueba del Alumno ---
# El estudiante intenta crear una cadena: [Nodo 1] -> [Nodo 2]

contenedor = Nodo("Datos Importantes 1")

# ERROR: El alumno intenta agregar el segundo nodo de esta forma:
contenedor = Nodo("Datos Importantes 2")

# Verificación
print(f"Contenido actual: {contenedor.valor}")
if contenedor.siguiente is None:
    print("ERROR: Se ha perdido la referencia al primer nodo. ¡Memory Leak conceptual!")

# TODO para el alumno: Corregir el código para que 'contenedor' mantenga el acceso al Nodo 1
# y el Nodo 1 apunte al Nodo 2.