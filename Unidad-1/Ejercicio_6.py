class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, inicio, fin):
        self.inicio = inicio # ERROR: Almacena la referencia directa
        self.fin = fin       # ERROR: Almacena la referencia directa

    def __str__(self):
        return f"Línea de {self.inicio} a {self.fin}"

# --- Prueba del Alumno ---
punto_a = Punto(0, 0)
punto_b = Punto(5, 5)

mi_linea = Linea(punto_a, punto_b)
print(f"Línea original: {mi_linea}")

# El alumno modifica uno de los puntos originales
punto_a.x = 10
punto_a.y = 10

print(f"Línea después de modificar el punto 'A': {mi_linea}")

# TODO: Corregir la clase Linea para que sea "inmutable" conceptualmente;
# es decir, que los cambios en los objetos Punto externos no afecten la línea una vez creada.