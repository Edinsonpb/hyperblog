import datetime

#ayer = ahora - datetime.timedelta(days=1)
#print("Ayer fue : " + str(ayer))

def run():
   ahora = datetime.datetime.utcnow()
   rutina = int(input("Escribe el numero de horas que dedicaras a un curso por cada dia :"))
   duracion = int(input("Escribe cuantas horas toma el curso :"))
   cantidaddias = round(duracion / rutina, 0)
   diasestudiar = datetime.timedelta(days=(cantidaddias))
   fechameta = ahora + diasestudiar
   print("Terminaras el : " + str(fechameta))

#    while diaacumulado < plazo:
#        #print(diacumulado)
#        diasestudiar = diaestudiar + 1
#        diaacumulado = ahora + diasestudiar
#        print("estudiar este dia : " + str(diaacumulado))


if __name__ == '__main__':
    run()