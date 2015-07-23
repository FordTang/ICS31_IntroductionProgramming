__author__ = 'dgk'
from collections import namedtuple
#  Ford Tang 46564602 and Michael Ragheb 66786623.  ICS 31 Lab sec 8.  Lab asst 6.

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 d:  Search the collection for selected cuisine
 t:  Search the collection for selected dish
 p:  Print all the restaurants
 c:  Change prices for the dishes served
 q:  Quit

Please enter a command:   """

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """    
    while True:        
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='c':
            n=float(input("Please enter percantage: "))
            Collection_change_prices(C,n)
        elif response == 'd':
            Collection_search_cuisine(C)
        elif response == 't':
            Collection_search_dish(C)
            
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")


##### Dish
Dish=namedtuple ("Dish", "name price cal")

def Dish_str (d:Dish)->str:
    return d.name+' ($'+str(d.price)+'): '+str(d.cal)+' cal'

def Dish_get_info() -> Dish:
    """ Prompt user for fields of Dish; create and return.
    """
    return Dish(
        input("Please enter the Dish name:  "),
        float(input("Please enter the price:  ")),
        int(input("Please enter the calorie(s):  ")))

def Dish_change_price(d:Dish,p:float)->Dish:
    return (Dish(d.name,d.price*(1+(p*0.01)),d.cal))


#f.1
def Dishlist_prices(dish: [Dish]) -> list:
        ''' Takes a list of dishes and returns a list of prices of the dishes
        '''
        price_list = []
        for i in dish:
            price_list.append(i.price)
        return price_list

#f.1
def Dishlist_calories(dish: [Dish]) -> list:
    calorie_list = []
    for i in dish:
        calorie_list.append(i.cal)
    return calorie_list

#### Menu
# A Menu is a list of Dishes

#f.1
def Menu_average(dish:[Dish]) -> float:
    '''Takes a list of dishes and returns the average price
    '''
    Prices = Dishlist_prices(dish)
    Total_Prices = 0.0
    for i in Prices:
        Total_Prices += i
    return Total_Prices/ len(Prices)

#f.1
def Menu_calories(dish:[Dish]) -> float:
    total_calories = 0.0
    dishes = Dishlist_calories(dish)
    for i in dishes:
        total_calories += i
    return total_calories/len(dishes)        

def Menu_change_price(d: list, p: float):
    for i in range(len(d)):
        d[i] = (Dish_change_price(d[i], p))
        
def Menu_str (m:list) -> str:
    result=''
    for i in m:
        result+=Dish_str(i)+"\n          "
    result += "\n"
    return result

def Menu_enter() -> list:
    result = []
    command = input("Would you like to add a dish? (y/n):  ")
    while (command.lower() == "y"):
        result.append(Dish_get_info())
        command = input("Would you like to add a dish? (y/n):  ")
    return result

#f.3
def Menu_dish_name(dishes: list, name: str) -> bool:
    for i in dishes:
        if name in i.name:
            return True
    return False


##### Restaurant
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

#f.1
def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " + Menu_str(self.menu) +
        "Average price:  $" + str(Menu_average(self.menu)) + ".   Average calories:  " + str(Menu_calories(self.menu)) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())    

#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]


#f.2
def Collection_search_by_cuisine(collection: list, cuisine: str) -> list:
    result = []
    for n in collection:
        if n.cuisine == cuisine:
            result.append(n)
    return result

def Collection_search_by_average(collection: list, average: float) -> list:
    result = []
    for n in collection:
        average_price = Menu_average(n.menu)
        if average_price < average:
            result.append(n)
    return result

#f.2
def Collection_search_cuisine(collection: list):
    # function prints Restaurants with specified cuisine along with average price
    cuisine_choice = str(input("Please enter the cuisine:  "))

    cuisine_list = Collection_search_by_cuisine(collection, cuisine_choice)
    print (Collection_str(cuisine_list))

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

#f.3
def Collection_search_dish(collection: list):
    dish_choice = str(input("Please enter the name of the dish:  "))

    restaurant_list = []
    for i in collection:
        if Menu_dish_name(i.menu, dish_choice):
            restaurant_list.append(i)
    print (Collection_str(restaurant_list))

#f

def Collection_change_prices(c:list,p:float):
    for i in c:
        Menu_change_price(i.menu,p)
    

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

restaurants()

