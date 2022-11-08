from random import randint


def fill_list():
    ile = int(input("Ile liczb wylosować? "))
    lista = []
    for i in range(0, ile):
        lista.append(randint(0, 100))
    print(lista)


fill_list()