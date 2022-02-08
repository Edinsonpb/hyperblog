def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos" + tipo_pesos + "tienes :")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 0)
    dolares = str(dolares)
    print("tienes" + dolares + "dolares")

menu = """
Bienvenido al conversor de monedas 👏

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    conversor("colombianos", 3960)
elif opcion == '2':
    conversor("argentinos", 37)
elif opcion == '3':
    conversor("mexicanos", 190)
else:
    print("Elige una opcion correcta")