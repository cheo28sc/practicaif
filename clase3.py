# new_users = "Esteban Segura Castro"

# users_name = new_users.split()
# print(users_name)

# user = "Esteban,38,Segura"
# user_1 = user.split(",")
# print(user_1)

#actualizacion de cadenas

# special = "Especial de la casa es Pasta"
# new_special = special.replace("Pasta","Pizza")
# print(new_special)


# value = "44,000"
# fixed_value = value.replace(".", ".")
# print(fixed_value)




#casting de variables
# print(type("HELLO"))
# print(type(10.5))
# print(type(10))
# print(type(True))


# age = "17"
# if int(age)  < 18:
#     print("you are too young")
    
    
    # position = 3
    # update = "your are now number "+str(position)+ "in the queue"
    # print (update)
    
    # price = 9.99
    # int(int(price))
    
    # member = True
    # value = int(member)
    # print(value)
    
#    # Python tambienproporciona las funciones list(), dict(), set(), y tuple()
#    choices = ["pizza", "burguer" , "SOPAS"]
#    unique = set(choices)
#    print (unique)
   
#    #funciones
# def greet_user():
#     print("Buenos Dias")
#     print("Hello Esteban")
    
# greet_user()
       
       
       
#        #creacion de parametros
# def greet_ron():
#     name="Esteban"
#     print(f"Hola,{name}")

# greet_ron()
       
       
# def greet(name):
    
#     print(f"Hola,{name}")
    
# greet("Esteban")
# greet("Keren")
# greet("Nana")
    
    
# def user_status(status):
#     username = "esteban"
#     print(f"{username} is {status}")
# user_status("activo")

# def double_number(number): 
#     result = number * 2
#     print (result)
# double_number (5)  
        
#         #valores devueltos
# def age_label(age):
#         label = "user age: " + age
#         return label
# edad = age_label("18")
# print(edad)
    
    
# def half_twice(number):
#         half = number/2
#         half_again = half / 2
#         return half_again
# result = half_twice(12)
# print(result)
    
#     #uso de multiples parametros
# def show_winner(first,second,third):
#         print ("first place: " + first)
#         print ("second place: " + second)
#         print ("third place:" + third)
# show_winner("Esteban", "Chris", " Paul ")
        
# def create_email(name, year):
#     return name + year + "@hotmail.com"
# email = create_email("csegura" , "1984")
# print (email)
        
        
# def get_final_price(price, tax):
#         return price + tax
# price = get_final_price(30,1.5)
# print(price)
        #alcanze de las funciones
# def add_bonus(salary):
            
#     bonus = 300
#     print (salary+bonus)
# add_bonus(1900)
            
#             #alcanze global de las funciones
shipping = 10
def calculate_total(cart):
    print (cart + shipping)
print (shipping)
calculate_total(54)
                
#                 #añadir condiciones a funciones
def add_shipping(cart):
    if cart < 100:
                    print(f"total: {cart+10}")
    else:
                    print(f"total:{cart}")
add_shipping(45)
add_shipping(200)