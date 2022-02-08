print("Convertidor de dolares a pesos colombianos")
dolares = input("cuantos dolares tienes ?: ")
dolares = float(dolares)
valor_dolar = 3875
pesos = dolares * valor_dolar
pesos = round(pesos, 0)
pesos = str(pesos)
print("Tienes $" + pesos)
