#declaraciones elif

# def calculate(operator, x, y):
#     if operator == "+":
#         print (x + y)
#     elif operator == "-":
#         print (x - y)
#     else:
#         print(f"unknown:{operator} ")
#         calculate("-", 40 , 30)
# def is_multiplayer(players):
#     print(len(players) == 2)
    
# players = ["Freddy", "Esteban"]
# is_multiplayer(players)
    
#funciones con bucles 
def onbord_passengers(bookings):
    Counter = 1
    while Counter <= bookings:
        print(f"Passengers {Counter} on board") 
        Counter += 1
        
onbord_passengers(15) 

def display_progress(total_files):
    for i in range(total_files):
        i += 1
        print(f"Downloading file {i} out of {total_files}")
        
display_progress(3)

#    la utilizacion de un bucle
def halve_price(cart):
    for price in cart:
        print (f"new price: {price/2}")
cart_list = [5, 20, 8]
halve_price(cart_list)   

def display_players(team):
    number  = 1
    for name in team:
        print (f"player {number}:{name} ")
        number += 1
team1 = ["kim", "lee", "Esteban"]
team2 = ["jos", "teban"]

display_players(team2)