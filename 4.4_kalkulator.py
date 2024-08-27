import sys
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def dodawanie(a,b):
    '''dodaje 2 liczby i zwraca ich sume'''
    logging.info(f"Dodaje {a} i {b}")
    print(f"Wynik to: {a+b}")

def odejmowanie(a,b):
    '''odejmuje 2 liczby i zwraca ich roznice'''
    logging.info(f"Odejmuje {a} od {b}")
    print(f"Wynik to: {a-b}")

def mnozenie(a,b):
    '''mnozy 2 liczby i zwraca ich rezultat'''
    logging.info(f"Mnoze {a} i {b}")
    print(f"Wynik to: {a*b}")

def dzielenie(a,b):
    '''dzieli 2 liczby i zwraca ich rezultat'''
    logging.info(f"Dziele {a} przez {b}")
    print(f"Wynik to: {a/b}")

if __name__ == "__main__":
    rodzaj_dzialania = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    skladnik_1 = int(input("Podaj skladnik 1: "))
    skladnik_2 = int(input("Podaj skladnik 2: "))
    
    if rodzaj_dzialania == '1':
        dodawanie(skladnik_1,skladnik_2)
    elif rodzaj_dzialania == '2':
        odejmowanie(skladnik_1,skladnik_2)
    elif rodzaj_dzialania == '3':
        mnozenie(skladnik_1,skladnik_2)
    else:
        dzielenie(skladnik_1, skladnik_2)
    

