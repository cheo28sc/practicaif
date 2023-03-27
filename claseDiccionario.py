#lista para almacenar una marca de una tienda pero no su sede, usamos dos listas

locations_list = ["NY","PARIS"]
print(locations_list)

#creacion de diccionario
locations = {
    "Sede" : "NY",
    "Marca" : "PARIS"
}
print(locations)

car_dat = {
    "Marca" : "Toyota",
    "Año"   : "2015",
    "Restauracion" : ["2011", "2018"],
    "Rentado" : False
}
print(car_dat)

actor_bio = {
    "Nombre" : "Esteban Segura",
    "conocido_por" : ["Todos los hombres van al cielo","Siempre mientes"]
}
print(actor_bio["Nombre"])

actor_name = actor_bio["Nombre"]
print(actor_name)

#Ejemplo para recorrer un diccionario con un bucle
players_scores = {
    "Esteban" : 13,
    "Juan"  : 20,
    "Pedro" : 34
}
for player in players_scores:
    print(players_scores[player])
    
    #actualizar valor de un diccionario
    tikect = {
        "Asiento" : 25,
        "Primera clase" : False
    }
    tikect ["Primera clase"] = True
    print(tikect)
    
    #para agregar una  clave ,cidificamos el diccionarioy luego el nombre de la clave
    tikect["windows"] = True
    print(tikect)
    
    #comprobar si un diccionario tiene una clave
    datos_personales = {
        "name" : "Esteban Segura",
        "Phone" : 8888888
        
    }
    print("name"in datos_personales)
    
    
    #eliminar una clave de un diccionario
    tikect = {
        "asiento" : 25,
        "primera clase" : False,
        "windows" : True
    }
    tikect.pop("windows")
    print(tikect)