from polinomio import Polinomio


def main():
    p1 = Polinomio()
    p1.poner_termino(2, 3)
    p1.poner_termino(3, 2)
    p1.poner_termino(4, 1)

    print("Se creo el polinomio correctamente")
    print( "P1(X)=", p1)


if __name__ == "__main__":
    main()