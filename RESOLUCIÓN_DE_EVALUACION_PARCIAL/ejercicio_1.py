#Calculo del tiempo:

# Tiempo faltante para las 22:15:30

#1. Entrada:
hora_limite_seg = 22 * 3600 + 15 *60 + 30  #CONVERSIÓN DE TIEMPO

hora_actual = input("Ingrese la hora actual en (HH:MM:SS): \n ")  #INGRESAR HORA ACTUAL

#2. PROCESO:
# SEPARAR EN PARTES: horas, minutos, segundos:
partes=hora_actual.split(":")
h= int(partes[0])
m= int(partes[1])
s= int(partes[2])

hora_actual_seg = h * 3600 + m*60 + s

#No debe ser mayor de la hora limite:
if hora_actual_seg >= hora_limite_seg:
    print("LA HORA INGRESADA ES MAYOR A LA HORA LIMITE")
else:
    DIFERENCIA = hora_limite_seg  - hora_actual_seg #HALLAR LA DIFERENCIA EN SEGUNDOS

    #convertir segundos a formato HH:MM:SS
    horas_falta = DIFERENCIA//3600
    minutos_falta = (DIFERENCIA % 3600)//60
    segundos_falta = DIFERENCIA % 60

#3. salida:
    print(f"El tiempo faltantepara las 22:15:30 es: \n  {horas_falta} horas :  {minutos_falta:02} minutos :  {segundos_falta} segundos")
