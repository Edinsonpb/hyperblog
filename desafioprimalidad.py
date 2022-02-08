num = int(input("escribe un numero "))

def factorial(num):
    if num - 1 < 0:
        print("Factorial de numero negativo no existe")

    elif num -1 == 0:
        return 1

    else:
        fact = 1
        while(num - 1 > 1):
            fact *= num-1
            num -= 1
        return fact

primo = factorial(num) + 1

if primo % num == 0:
    print("es un numero primo")
else:
    print("no es numero primo")

#print("factorial de " + str(num-1) + " es : " + str(factorial(num)))

