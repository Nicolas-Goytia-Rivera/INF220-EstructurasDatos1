class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"{self.color} {self.marca} {self.modelo}"

class Garaje:
    def __init__(self):
        self.automoviles = []

    def agregar_automovil(self, auto):
        self.automoviles.append(auto)

    def mostrar_automoviles(self):
        print("Automóviles en el garaje:")
        for i, auto in enumerate(self.automoviles):
            print(f"  {i+1}. {auto}")

# --- Prueba del Alumno ---
mi_garaje = Garaje()

# El alumno intenta añadir dos coches diferentes
auto_temporal = Automovil("Toyota", "Corolla", "Rojo")
mi_garaje.agregar_automovil(auto_temporal)

# ERROR: Reutiliza la misma variable para 'crear' otro coche, pero en realidad solo modifica el objeto existente
auto_temporal.marca = "Honda"
auto_temporal.modelo = "Civic"
auto_temporal.color = "Azul"
mi_garaje.agregar_automovil(auto_temporal)

mi_garaje.mostrar_automoviles()

# TODO: Corregir el código para que el garaje contenga dos automóviles distintos con sus respectivas propiedades.