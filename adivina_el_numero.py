import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un nùmero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un nùmero mas grande")
        else:
            print("elige un numero mas pequeño")
        numero_elegido = int(input("Elige otro numero: "))
    print("ganaste!")


if __name__ == '__main__':
    run()