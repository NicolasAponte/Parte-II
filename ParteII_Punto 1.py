# -*- coding: utf-8 -*-

# In[]
#Se eligió Python como lenguaje de programación
def mantenimiento(fecha_inicio,promedio_km_diarios):
    #fecha_inicio: DD-MM-YYYY
    arreglo_fecha=fecha_inicio.split('-')
    calendario=[]
    dias_mantenimiento = int(5000/promedio_km_diarios)
    dias = arreglo_fecha[0]
    mes = int(arreglo_fecha[1])
    anio = arreglo_fecha[2]
    for i in range(0,50):
        dias = int(dias) + dias_mantenimiento
        if(dias > 31):
            mes_adicion = int(dias/31)
            dias = round(((dias/31)- mes_adicion)*31)
            mes = mes + mes_adicion
        if(mes > 12):
            mes = mes - 12 
            anio = int(anio) + 1
        calendario.append(str(dias)+"-"+str(mes) +"-"+str(anio))
        
    print(calendario)
        
mantenimiento('31-01-2020', 5000)

