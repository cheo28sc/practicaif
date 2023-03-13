#una funcion que solicite año mes y dia y almacene en una tupla y luego retornar, mostrar en consola

# def cargar_fecha():
#     dd = int(input("ingrese numero de dia "))
#     mm = int(input("ingrese numero de mes "))
#     aa = int(input("ingrese numero de año "))
#     return(dd,mm,aa)

# def imprimir_fecha(fecha):
#     print (fecha[0],fecha[1],fecha[2], sep="/")
    
# #bloque principal   
# fecha = cargar_fecha()
# imprimir_fecha(fecha)
        
    
#empaqietado y desempaquetado de tuplas

x=10
y=30
punto = (x,y)   

print (punto) 

#desempaquetar 3 variables
print("*********************************")
fecha = (25,"Diciembre", 2023)
print (fecha)

dd,mm,aa = fecha
print ("Dia: ", dd)
print ("Mes: ", mm)
print ("Año: ", aa)
print("*********************************")