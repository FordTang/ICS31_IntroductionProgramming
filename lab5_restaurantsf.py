__author__ = 'dgk'
from collections import namedtuple


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

#### Menu
# A Menu is a list of Dishes
def Menu_change_price(d: list, p: float):
    for i in range(len(d)):
        d[i] = (Dish_change_price(d[i], p))
        
def Menu_str (m:list) -> str:
    result=''
    for i in m:
        result+=Dish_str(i)+"\n          "
    result+='\n'
    return result

def Menu_enter() -> list:
    result = []
    command = input("Would you like to add a dish? (y/n):  ")
    while (command.lower() == "y"):
        result.append(Dish_get_info())
        command = input("Would you like to add a dish? (y/n):  ")
    return result

##### Restaurant
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " + Menu_str(self.menu))

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

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C
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

