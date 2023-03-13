#Problema 1 definir una lista imprima en pantalla

# lista = []

# for x in range (5):
#     valor =  int (input("ingrese un valor entero: "))
#     lista.append(valor)
#     #imprimir
# print (lista)


#problema 2
lista2 = []

valor2 =  int(input("ingrese un valor: (0 para finalizar)"))

while valor2 != 0:
    
    lista2.append(valor2)
    valor2 = int(input("ingrese un valor: (0 para finalizar)")) 
print ("tamaño de la lista ", len(lista2))

