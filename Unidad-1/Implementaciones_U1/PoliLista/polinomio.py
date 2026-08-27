from listaP import Lista
 
 
class Polinomio:
 
    def __init__(self):
        self._pol = Lista()
 
 
    def _buscar_exponente(self, exp):
        
        sentinel = self._pol.siguiente(self._pol.fin())
 
        if self._pol.vacia():
            return sentinel
 
        dir_actual = self._pol.siguiente(self._pol.primero())
        while dir_actual != sentinel:
            if self._pol.recupera(dir_actual) == exp:
                return dir_actual
            dir_actual = self._pol.siguiente(
                self._pol.siguiente(dir_actual)
            )
 
        return sentinel
 
    def _buscar_termino_n(self, i):

        if self._pol.vacia():
            raise Exception("No existen términos.")
 
        dir_actual = self._pol.primero()
        numero = 1
 
        while numero != i:
            numero += 1
            dir_actual = self._pol.siguiente(
                self._pol.siguiente(dir_actual)
            )
 
        return dir_actual
 
    def es_cero(self):
        return self._pol.vacia()
 
    def grado(self):
        
        if self._pol.vacia():
            raise Exception(
                "No existe ningún término en el polinomio."
            )
 
        sentinel = self._pol.siguiente(self._pol.fin())

        dir_actual = self._pol.siguiente(self._pol.primero())
        max_grado = self._pol.recupera(dir_actual)
 
        dir_actual = self._pol.siguiente(self._pol.siguiente(dir_actual))
 
        while dir_actual != sentinel:
            exponente_actual = self._pol.recupera(dir_actual)
            if exponente_actual > max_grado:
                max_grado = exponente_actual
            dir_actual = self._pol.siguiente(
                self._pol.siguiente(dir_actual)
            )
 
        return max_grado
 
    def coeficiente(self, exp):

        dir_exp = self._buscar_exponente(exp)
        sentinel = self._pol.siguiente(self._pol.fin())
 
        if dir_exp != sentinel:
            return self._pol.recupera(self._pol.anterior(dir_exp))
 
        raise Exception("No existe ese término en el polinomio.")
 
    def numero_terminos(self):
        """Retorna la cantidad de términos del polinomio."""
        return self._pol.longitud_lista() // 2
 
    def exponente(self, nro_ter):
        
        dir_coef = self._buscar_termino_n(nro_ter)
        sentinel = self._pol.siguiente(self._pol.fin())
 
        if dir_coef != sentinel:
            return self._pol.recupera(self._pol.siguiente(dir_coef))
 
        raise Exception("No existe ese término en el polinomio.")
 
    def asignar_coeficiente(self, coef, exp):
        
        dir_exp = self._buscar_exponente(exp)
        sentinel = self._pol.siguiente(self._pol.fin())
 
        if dir_exp == sentinel:
            raise Exception("No existe ese término en el polinomio.")
 
        dir_coef = self._pol.anterior(dir_exp)
        self._pol.modifica(dir_coef, coef)
 
        if coef == 0:
            self._pol.suprime(dir_exp)
            self._pol.suprime(dir_coef)
 
    def poner_termino(self, coef, exp):
        
        if coef == 0:
            return
 
        dir_exp = self._buscar_exponente(exp)
        sentinel = self._pol.siguiente(self._pol.fin())
 
        if dir_exp != sentinel:
            dir_coef = self._pol.anterior(dir_exp)
            nuevo_coef = self._pol.recupera(dir_coef) + coef
            self._pol.modifica(dir_coef, nuevo_coef)
 
            if self._pol.recupera(dir_coef) == 0:
                self._pol.suprime(dir_exp)
                self._pol.suprime(dir_coef)
        else:
            self._pol.inserta_ultimo(coef)
            self._pol.inserta_ultimo(exp)

    def _limpiar(self):
        
        while not self.es_cero():
            exp = self.exponente(1)
            self.poner_termino(-self.coeficiente(exp), exp)
 
    def suma(self, p1, p2):

        self._limpiar()
 
        for i in range(1, p1.numero_terminos() + 1):
            ex = p1.exponente(i)
            self.poner_termino(p1.coeficiente(ex), ex)
 
        for i in range(1, p2.numero_terminos() + 1):
            ex = p2.exponente(i)
            self.poner_termino(p2.coeficiente(ex), ex)
 
    def resta(self, p1, p2):
        
        self._limpiar()
 
        for i in range(1, p1.numero_terminos() + 1):
            ex = p1.exponente(i)
            self.poner_termino(p1.coeficiente(ex), ex)
 
        for i in range(1, p2.numero_terminos() + 1):
            ex = p2.exponente(i)
            self.poner_termino(-p2.coeficiente(ex), ex)
 
    def multiplicacion(self, p1, p2):
        
        self._limpiar()
 
        for i in range(1, p1.numero_terminos() + 1):
            ex1 = p1.exponente(i)
            co1 = p1.coeficiente(ex1)
 
            for j in range(1, p2.numero_terminos() + 1):
                ex2 = p2.exponente(j)
                co2 = p2.coeficiente(ex2)
                self.poner_termino(co1 * co2, ex1 + ex2)
 
    
    def evaluar(self, x):
        
        resultado = 0.0
        for i in range(1, self.numero_terminos() + 1):
            exp = self.exponente(i)
            coef = self.coeficiente(exp)
            resultado += coef * (x ** exp)
        return resultado
 
 
    def __str__(self):
        
        if self.es_cero():
            return "P(X) = 0"
 
        exp = self.exponente(1)
        coef = self.coeficiente(exp)
        cadena = f"P(X) = {coef}X^{exp}"
 
        for i in range(2, self.numero_terminos() + 1):
            exp = self.exponente(i)
            coef = self.coeficiente(exp)
            if coef > 0:
                cadena += f" + {coef}X^{exp}"
            else:
                cadena += f" - {-coef}X^{exp}"
 
        return cadena
 
    def __repr__(self):
        return self.__str__()
 