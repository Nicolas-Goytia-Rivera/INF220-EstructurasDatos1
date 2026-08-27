class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # ERROR: Lógica invertida
        return len(self.items) > 0

    def push(self, item):
        # ERROR: No está agregando el item recibido
        self.items = [item]

    def pop(self):
        # ERROR: No verifica si hay elementos antes de borrar
        # y no retorna el elemento eliminado
        self.items.remove(-1)

# --- Prueba del Alumno ---
mi_pila = Stack()
mi_pila.push("A")
mi_pila.push("B")

print("¿Está vacía?", mi_pila.is_empty())
print("Elemento sacado:", mi_pila.pop())

# TODO: Corregir la clase Stack para que cumpla con el comportamiento LIFO