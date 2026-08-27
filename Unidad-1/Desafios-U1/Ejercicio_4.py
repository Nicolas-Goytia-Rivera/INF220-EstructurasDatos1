class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Circunferencia:
    def __init__(self, centro, radio):
        self.centro = centro # ERROR: Se asigna la referencia directa al objeto Punto
        self.radio = radio

    def __str__(self):
        return f"Circunferencia con centro en {self.centro} y radio {self.radio}"

# --- Prueba del Alumno ---
mi_punto_original = Punto(1, 2)
mi_circunferencia = Circunferencia(mi_punto_original, 5)

print(f"Circunferencia inicial: {mi_circunferencia}")

# El alumno modifica el punto original
mi_punto_original.x = 10
mi_punto_original.y = 20

print(f"Circunferencia después de modificar el punto original: {mi_circunferencia}")

# TODO: Corregir la clase Circunferencia para que su centro no cambie si el Punto original es modificado.
# Es decir, la Circunferencia debe tener su propia copia de las coordenadas del centro.