"""
lista.py
--------
Lista enlazada simple implementada con nodos (equivalente a lista con
punteros en C++).  Sigue las convenciones de estilo PEP-8.
"""
 
 
class Nodo:
 
    def __init__(self):
        self.elemento = None
        self.sig = None
 
 
class Lista:
 
    def __init__(self):
        self.longitud = 0
        self._ptr_elementos = None

    def fin(self):

        dir_fin = self._ptr_elementos
        if dir_fin is not None:
            while dir_fin.sig is not None:
                dir_fin = dir_fin.sig
        return dir_fin
 
    def primero(self):

        return self._ptr_elementos
 
    def siguiente(self, dir):

        if dir is None:
            return None
        return dir.sig
 
    def anterior(self, dir):

        if dir is self._ptr_elementos or dir is None:
            return None
        ant = self._ptr_elementos
        while ant.sig is not dir:
            ant = ant.sig
        return ant
 
    def vacia(self):
        return self.longitud == 0
 
    def recupera(self, dir):
        if self.vacia():
            raise Exception("Lista vacía.")
        return dir.elemento
 
    def longitud_lista(self):
        return self.longitud

 
    def inserta(self, dir, elem):
        
        nodo = Nodo()
        nodo.elemento = elem
        nodo.sig = dir
 
        ant = self.anterior(dir)
        if ant is None:
            self._ptr_elementos = nodo
        else:
            ant.sig = nodo
 
        self.longitud += 1
 
    def inserta_primero(self, elem):
       
        nodo = Nodo()
        nodo.elemento = elem
        nodo.sig = self._ptr_elementos
        self._ptr_elementos = nodo
        self.longitud += 1
 
    def inserta_ultimo(self, elem):
      
        nodo = Nodo()
        nodo.elemento = elem
        nodo.sig = None
 
        if self.longitud != 0:
            self.fin().sig = nodo
        else:
            self._ptr_elementos = nodo
 
        self.longitud += 1
 
    def suprime(self, dir):
        
        if self.longitud == 0:
            raise Exception("Lista vacía.")
 
        if dir is self._ptr_elementos:
            self._ptr_elementos = self._ptr_elementos.sig
        else:
            ant = self.anterior(dir)
            ant.sig = self.siguiente(dir)
 
        
        self.longitud -= 1
 
    def modifica(self, dir, elem):
        
        if self.vacia():
            raise Exception("Lista vacía.")
        dir.elemento = elem