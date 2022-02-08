import datetime

#while break y continuo
#ayer = ahora - datetime.timedelta(days=1)

def run():
   
   premioporpeso = 400
   apuestadiaria = int(input("Digita el valor que apuestas diario : "))
   premio = premioporpeso * apuestadiaria
   diasapuesta = 1
   acumuladoapuesta = apuestadiaria * diasapuesta

   while acumuladoapuesta < premio:
      if diasapuesta == 365:
         break
      diasapuesta += 1
      acumuladoapuesta = apuestadiaria * diasapuesta
      print(str("has apostado por " + str(diasapuesta) + "dias"))
      print("has apostado : " + str(acumuladoapuesta))


if __name__ == '__main__':
   run()