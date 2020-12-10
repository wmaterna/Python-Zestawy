# SPECYFIKACJA PROBELMU:
# Znajdywania rozwiązań równania liniowego ax+by+c = 0
# DANE WEJŚCIOWE:
# Trzy liczby a,b,c stanowiące o równianiu
# DANE WYJŚCIOWE:
# Rozwiązanie w postaci komunikatu

# Lista kroków:
# K01: Wczytaj a, b, c
# K02: Sprawdź, które elemety są równe zero, jeżeli:
# a,b,c = 0 wypisz brak rozwiazania,
# a, b = 0 brak rozwiazania,
# a,c = 0 wypisz y = 0
# a = 0 wypisz y = -c/b
# b,c = 0 wypisz x = 0
# b = 0 wypisz x =  -c/a
# c = 0 wypisz y =  -a/b x
# zaden z elemenow nie równa się 0 wypisz y = -c / b +  -a / b x
# K03: Zakoncz algorytm


def solve1(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Brak rozwiązań")
            else:
                print("Brak rozwiązań")
        else:
            if c == 0:
                print("y = 0")
            else:
                print("y = ", -c/b)
    else:
        if b == 0:
            if c == 0:
                print("x = 0")
            else:
                print("x = ", -c/a)
        else:
            if c == 0:
                print("y = ", -a/b, "x")
            else:
                print("y = ", -c / b, "+ ", -a / b,"x")



solve1(1,3,6)
solve1(0,6,9)
solve1(1,0,0)

