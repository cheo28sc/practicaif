movies  = ["vertigo", "Chuky", 1985 , 2019]
#las tuplas son para agrupar datos relacionados
movies_tupla = [("vertigo",1985), ("Chuky", 2019)]

vertigo_data = ("vertigo",1985)
print (movies_tupla)

user_data = ("Esteban", 1984, "Segura")
print (user_data)

#nos devuelve multiples valores
movies_tupla = [("vertigo",1985), ("Chuky", 2019), ("Terminaitor", 2000)]
movies_tupla[2] = "ejemplo"
favorite = movies_tupla[2]
print(movies_tupla)

len = len(movies_tupla[1])
print(len)
#    nos devuelven multiples valores de una funcion
def get_score_datos(score_list):
    highest_score = max(score_list)
    lowest_score = min(score_list)
    return highest_score, lowest_score
scores = [31, 23, 35]
data = get_score_datos(scores)
print (data)
highest = data[0]
smallest = data[1]

print (f"smallest score: {smallest}" )
print (f"highest score: {highest} ")

#ordenamiento

def get_scores_datos(score_list):
    highest_score = sorted(score_list)
    
    return highest_score
scores = [31, 23, 35]
data = get_scores_datos(scores)
print (data)

first = data [0]
second = data [1]
third = data [2]
print(f"first:{first} ")
print(f"second: {second}")
print(f"third: {third}")