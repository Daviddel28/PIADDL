from datetime import datetime, timedelta

hh = int(input("Hora de salida (HH): "))
mm = int(input("Minutos (MM): "))
ss = int(input("Segundos (SS): "))
T  = int(input("Tiempo de viaje en segundos (T): "))

salida = datetime(2000, 1, 1, hh, mm, ss)
llegada = salida + timedelta(seconds=T)
print("Hora de llegada:", llegada.strftime("%H:%M:%S"))