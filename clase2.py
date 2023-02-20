# keep_going = True
# while keep_going == True:
#     print ("and again")

# keep_going = False
# print ("one more time")

#controlar bucle

# counter = 1
# while counter < 4:
#     print ("counter")
#     counter += 1 
    
    
    
# inter_shipping = True
    
# total = 150
# shipping_cost = 0

# if inter_shipping:
#         shipping_cost += 20
#         print  ("internacinal base cost applied")
#         if total <= 50:
#             shipping_cost += 20
#         elif total <= 100:
#             shipping_cost += 15
# else:
#     shipping_cost += 5
#     print (f"shipping cost:  {shipping_cost}")

# account = 100
# interest_rate = 0.004
# years = 3
# print (f"initial amount:{account}")
# counter = 1
# while counter <= years:
#     accrued_interest = account * interest_rate
#     account += accrued_interest
#     print (f"years{counter}: {account} ")
#     counter += 1

#listas parencites cuadrados y array
# age = [25,26, 27, 27]
# age [2] = 40
# print (age[2])

# todo = ["leer", "tareas", "codigos"]
# print(todo)

# scores = [24, 23]
# scores.append (25)
# print (scores)
# users = ["luis", "juan", "esteban"]
# users.append("esteban")
# print (users)

# shopping = ["limon", "mango", "manzana"]
# shopping.insert(0,"sandia")
# shopping.insert(1,"pera")
# print (shopping)

# todo = ["leer", "trabajo", "tarea"]
# todo.pop(1)
# removed = todo.pop(1)
# print (todo)
# print (removed)

# final_score = [17,22,23,34,13]

# for score in final_score:
#     print (score)
#     print ("--------")
    
#     data_points = [99,99,99,99]
#     for data in data_points:
#         print (data+1)

# users = []
# number_of_users = len(users)
# if number_of_users > 0:

#   print (f"online users : {number_of_users}")
# else:
#     print ("offline app")
    



# humidity_level = [87,83,88,87]
# humidity_level.insert(0.90)
# humidity_level.pop()
# print (humidity_level)



#encontrar los min y max
# humidity_level = [87,83,88,87]
# min = min(humidity_level)
# max = max(humidity_level)
# sorted = sorted(humidity_level)
# sum = sum(humidity_level)
# print (max)
# print (min)
# print(sorted(humidity_level))



# dataset1 =  [1,2,3,]
# dataset2 = [4,5]
# combined = dataset1 + dataset2
# print (combined)


humidity_level = [87,83,88,87,89,100,101,107,107]
count = humidity_level.count(107)
print (count)
find = 107
if find in humidity_level:
    print (f"{find} se encuentra en la lista")
else:
    print (f"{find} no se encuentra en la lista")
    
    
    