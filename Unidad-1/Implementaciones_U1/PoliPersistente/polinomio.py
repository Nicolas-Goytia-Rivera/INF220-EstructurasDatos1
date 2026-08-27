class PolinomioPersistente:

    def __init__(self, nombre_archivo="polinomio.txt"): # decirles que aqui ustedes pueden poner el nombre del archivo que quieran
        self._terminos = {}
        self.nt = 0
        self.nombre_archivo = nombre_archivo
        self._cargar()

    def _guardar(self):
        with open(self.nombre_archivo, "w", encoding="utf-8") as archivo:
            for exponente, coeficiente in self._terminos.items():
                archivo.write(f"{exponente},{coeficiente}\n")

    def _cargar(self):
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue

                    partes = linea.split(",")
                    if len(partes) != 2:
                        continue

                    exponente = int(partes[0])
                    coeficiente = int(partes[1])

                    self._terminos[exponente] = coeficiente
                    self.nt += 1
        except FileNotFoundError:
            pass

    def borrar_archivo(self):
        try:
            import os
            os.remove(self.nombre_archivo)
        except FileNotFoundError:
            pass

    def mostrar_archivo(self):
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as archivo:
                print(f"Contenido de {self.nombre_archivo}:")
                print("exponente | coeficiente")
                print("-" * 25)

                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        partes = linea.split(",")
                        if len(partes) == 2:
                            print(f"{partes[0]:>9} | {partes[1]:>11}")
        except FileNotFoundError:
            print("No se encontró el archivo.")

    def es_cero(self):
        return self.nt == 0

    def poner_termino(self, coeficiente, exponente):
        
        if exponente < 0:
            raise ValueError("El exponente no puede ser negativo.")

        if coeficiente == 0:
            return

        if exponente in self._terminos:
            self._terminos[exponente] += coeficiente

            if self._terminos[exponente] == 0:
                del self._terminos[exponente]
                self.nt -= 1
        else:
            self._terminos[exponente] = coeficiente
            self.nt += 1

        self._guardar()

    def eliminar_termino(self, exponente):
        if exponente in self._terminos:
            del self._terminos[exponente]
            self.nt -= 1
            self._guardar()

    def coeficiente(self, exponente):
        return self._terminos.get(exponente, 0)

    def grado(self):
        if self.es_cero():
            return -1
        return max(self._terminos.keys())

    def evaluar(self, x):
        resultado = 0

        for exponente, coeficiente in self._terminos.items():
            resultado += coeficiente * (x ** exponente)

        return resultado

    def derivada(self, archivo_resultado="derivada.txt"):
       
        derivado = PolinomioPersistente(archivo_resultado)
        derivado._terminos = {}
        derivado.nt = 0
        derivado._guardar()

        for exponente, coeficiente in self._terminos.items():
            if exponente > 0:
                derivado.poner_termino(
                    coeficiente * exponente,
                    exponente - 1
                )

        return derivado

    def sumar(self, otro, archivo_resultado="suma.txt"):
        
        resultado = PolinomioPersistente(archivo_resultado)
        resultado._terminos = {}
        resultado.nt = 0
        resultado._guardar()

        for exponente, coeficiente in self._terminos.items():
            resultado.poner_termino(coeficiente, exponente)

        for exponente, coeficiente in otro._terminos.items():
            resultado.poner_termino(coeficiente, exponente)

        return resultado

    def restar(self, otro, archivo_resultado="resta.txt"):
        
        resultado = PolinomioPersistente(archivo_resultado)
        resultado._terminos = {}
        resultado.nt = 0
        resultado._guardar()

        for exponente, coeficiente in self._terminos.items():
            resultado.poner_termino(coeficiente, exponente)

        for exponente, coeficiente in otro._terminos.items():
            resultado.poner_termino(-coeficiente, exponente)

        return resultado

    def multiplicar(self, otro, archivo_resultado="producto.txt"):
        
        resultado = PolinomioPersistente(archivo_resultado)
        resultado._terminos = {}
        resultado.nt = 0
        resultado._guardar()

        for exp_1, coef_1 in self._terminos.items():
            for exp_2, coef_2 in otro._terminos.items():
                resultado.poner_termino(
                    coef_1 * coef_2,
                    exp_1 + exp_2
                )

        return resultado

    def __str__(self):
        if self.es_cero():
            return "0"

        partes = []

        for exponente in sorted(self._terminos.keys(), reverse=True):
            coeficiente = self._terminos[exponente]

            if coeficiente == 0:
                continue

            signo = "+" if coeficiente > 0 else "-"
            valor = abs(coeficiente)

            if exponente == 0:
                termino = f"{valor}"
            elif exponente == 1:
                termino = "x" if valor == 1 else f"{valor}x"
            else:
                termino = f"x^{exponente}" if valor == 1 else f"{valor}x^{exponente}"

            partes.append((signo, termino))

        resultado = ""

        for i, (signo, termino) in enumerate(partes):
            if i == 0:
                resultado += f"-{termino}" if signo == "-" else termino
            else:
                resultado += f" {signo} {termino}"

        return resultado