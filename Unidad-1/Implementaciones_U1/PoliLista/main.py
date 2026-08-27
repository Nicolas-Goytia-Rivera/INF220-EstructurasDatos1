from polinomio import Polinomio

def main():
    p1 = Polinomio()
    p2 = Polinomio()

    p1.poner_termino(3, 2)
    p1.poner_termino(5, 1)
    p1.poner_termino(-2, 0)

    p2.poner_termino(4, 3)
    p2.poner_termino(-1, 2)
    p2.poner_termino(2, 0)

    print("P1:", p1)
    print("P2:", p2)

    suma = Polinomio()
    suma.suma(p1, p2)
    print("P1 + P2:", suma)

    resta = Polinomio()
    resta.resta(p1, p2)
    print("P1 - P2:", resta)

    producto = Polinomio()
    producto.multiplicacion(p1, p2)
    print("P1 * P2:", producto)

if __name__ == "__main__":
    main()