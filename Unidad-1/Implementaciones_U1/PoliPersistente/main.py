from polinomio import PolinomioPersistente

def main():
    p1 = PolinomioPersistente()
    p1.poner_termino(2, 3)
    p1.poner_termino(3, 2) 
    p1.poner_termino(4, 0) 
    p1.mostrar_archivo()

if __name__ == "__main__":
    main() 
