class Polinomio:
    def __init__(self):
        self._terminos = {}
        self.nt = 0  # número de términos

    def es_cero(self):
        return self.nt == 0

    def poner_termino(self, coeficiente, exponente):
        if exponente < 0:
            raise ValueError("El exponente no puede ser negativo.")
        if coeficiente == 0:
            return

        encontrado = False
        for exp in self._terminos:
            if exp == exponente:
                self._terminos[exp] += coeficiente
                encontrado = True
                if self._terminos[exp] == 0:
                    del self._terminos[exp]
                    self.nt -= 1
                break

        if not encontrado:
            self._terminos[exponente] = coeficiente
            self.nt += 1

    def eliminar_termino(self, exponente):
        for exp in self._terminos:
            if exp == exponente:
                del self._terminos[exp]
                self.nt -= 1
                break

    def coeficiente(self, exponente):
        for exp, coef in self._terminos.items():
            if exp == exponente:
                return coef
        return 0

    def grado(self):
        if self.es_cero():
            return -1
        maximo = -1
        for exp in self._terminos:
            if exp > maximo:
                maximo = exp
        return maximo

    def evaluar(self, x):
        resultado = 0
        for exponente, coeficiente in self._terminos.items():
            potencia = 1
            for _ in range(exponente):
                potencia *= x
            resultado += coeficiente * potencia
        return resultado

    def derivada(self):
        derivado = Polinomio()
        for exponente, coeficiente in self._terminos.items():
            if exponente > 0:
                derivado.poner_termino(coeficiente * exponente, exponente - 1)
        return derivado

    def sumar(self, otro):
        resultado = Polinomio()
        for exponente, coeficiente in self._terminos.items():
            resultado.poner_termino(coeficiente, exponente)
        for exponente, coeficiente in otro._terminos.items():
            resultado.poner_termino(coeficiente, exponente)
        return resultado

    def restar(self, otro):
        resultado = Polinomio()
        for exponente, coeficiente in self._terminos.items():
            resultado.poner_termino(coeficiente, exponente)
        for exponente, coeficiente in otro._terminos.items():
            resultado.poner_termino(-coeficiente, exponente)
        return resultado

    def multiplicar(self, otro):
        resultado = Polinomio()
        for exp_1, coef_1 in self._terminos.items():
            for exp_2, coef_2 in otro._terminos.items():
                resultado.poner_termino(coef_1 * coef_2, exp_1 + exp_2)
        return resultado

    def __str__(self):
        if self.es_cero():
            return "0"

        claves = []
        for exp in self._terminos:
            claves.append(exp)

        for i in range(len(claves) - 1):
            for j in range(len(claves) - 1 - i):
                if claves[j] < claves[j + 1]:
                    aux = claves[j]
                    claves[j] = claves[j + 1]
                    claves[j + 1] = aux

        resultado = ""
        primer_termino = True

        for exp in claves:
            coef = self._terminos[exp]
            if coef == 0:
                continue

            valor = coef
            if valor < 0:
                valor = -valor

            if exp == 0:
                termino = str(valor)
            elif exp == 1:
                if valor == 1:
                    termino = "x"
                else:
                    termino = str(valor) + "x"
            else:
                if valor == 1:
                    termino = "x^" + str(exp)
                else:
                    termino = str(valor) + "x^" + str(exp)

            if primer_termino:
                if coef < 0:
                    resultado = "-" + termino
                else:
                    resultado = termino
                primer_termino = False
            else:
                if coef < 0:
                    resultado = resultado + " - " + termino
                else:
                    resultado = resultado + " + " + termino

        return resultado