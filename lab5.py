#Ray Chou 67255516 and Ford Tang 46564602  ICS 31 Lab sec 8 asst 5

#Part c
print("---Part c.2--")
print("")
#c.2
from collections import namedtuple

Dish=namedtuple ("Dish", " name price cal")

D1=Dish("hamburger",5.99,1000)
D2=Dish("fries",2.99,380)
D3=Dish("salad",5.99,400)

def Dish_str (d:Dish)->str:
    return d.name+' ($'+str(d.price)+'): '+str(d.cal)+' cal'
assert Dish_str(D1)=="hamburger ($5.99): 1000 cal"

#c.3
print("---Part c.3--")
print("")
def Dish_same (d1:Dish,d2:Dish)->bool:
    return (d1.name==d2.name)and (d1.cal==d2.cal)
assert (Dish_same(D1,D1))==True
assert (Dish_same(D1,Dish(D1.name,6.99,D1.cal)))==True
assert (Dish_same(D1,D2))==False 

#c.4
print("---Part c.4--")
print("")
def Dish_change_price(d:Dish,p:float)->Dish:
    return (Dish(d.name,d.price*(1+(p*0.01)),d.cal))
assert(Dish_change_price(D1,100))==Dish(name='hamburger', price=11.98, cal=1000)
#c.5
print("---Part c.5--")
print("")
def Dish_is_cheap(d:Dish,n:float)->bool:
    return (d.price<n)
assert(Dish_is_cheap(D1,4))==False

#c.6
print("---Part c.6--")
print("")
DL=[
    Dish("hamburger",5.99,1000),
    Dish("fries",2.99,380),
    Dish("salad",5.99,400),
    Dish("rice",1.00,150),
    Dish("sloppy joe's", 4.00, 600)
    ]

DL2=[
    Dish("noodle",0.99,200),
    Dish("sandwich",6.99,700),
    Dish("cake",3.99,750),
    Dish("ice cream",1.99,300)
    ]
DL.extend(DL2)
print(DL)

def Dishlist_display(d:list)->str:
    result=''
    for i in d:
        result+=(Dish_str(i) + '\n')
    return result
assert Dishlist_display(DL)=='''hamburger ($5.99): 1000 cal
fries ($2.99): 380 cal
salad ($5.99): 400 cal
rice ($1.0): 150 cal
sloppy joe's ($4.0): 600 cal
noodle ($0.99): 200 cal
sandwich ($6.99): 700 cal
cake ($3.99): 750 cal
ice cream ($1.99): 300 cal
'''

#c.7
print("---Part c.7--")
print("")
def Dishlist_all_cheap(d:list,n:float)->bool:
    for i in d:
        if Dish_is_cheap(i,n) == False:
            return False
    return True

assert(Dishlist_all_cheap(DL2,.50))==False
#c.8
print("---Part c.8--")
print("")
def Dishlist_change_price(d:list,n:float)->list:
    result=[]
    for i in d:
        result.append(Dish_change_price(i, n))
    return result
assert(Dishlist_change_price(DL2,50))==[Dish(name='noodle', price=1.4849999999999999, cal=200), Dish(name='sandwich', price=10.485, cal=700), Dish(name='cake', price=5.985, cal=750), Dish(name='ice cream', price=2.985, cal=300)]

#c.9
print("---Part c.9--")
print("")
def Dishlist_prices(d:list)->list:
    result=[]
    for i in d:
        result.append(i.price)
    return result
assert(Dishlist_prices(DL2))==[0.99, 6.99, 3.99, 1.99]
#c.10
print("---Part c.10--")
print("")
def Dishlist_average(d:list)->float:
    return (sum(Dishlist_prices(d))/len(d))
assert(Dishlist_average(DL2))==3.49
#c.11
print("---Part c.11--")
print("")
def Dishlist_keep_cheap(d:list,n:float)->list:
    result=[]
    for i in d:
        if Dish_is_cheap(i,n):
            result.append(i)
    return result
assert(Dishlist_keep_cheap(DL2,2.00))==[Dish(name='noodle', price=0.99, cal=200), Dish(name='ice cream', price=1.99, cal=300)]
#c.12
print("---Part c.12--")
print("")

DL3=[
    Dish("hamburger",5.99,1000),
    Dish("fries",2.99,380),
    Dish("salad",5.99,400),
    Dish("rice",1.00,150),
    Dish("sloppy joe's", 4.00, 600),
    Dish("noodle",0.99,200),
    Dish("sandwich",6.99,700),
    Dish("cake",3.99,750),
    Dish("ice cream sandwich",2.99,400),
    Dish("cheeseburger",6.49,1100),
    Dish("chili cheese fries",4.99,680),
    Dish("tuna salad",7.99,600),
    Dish("fried rice",5.00,550),
    Dish("Philly Cheese Steak Sandwich", 7.00, 1200),
    Dish("noodle soup",4.99,600),
    Dish("egg sandwich",4.99,700),
    Dish("cheesecake",5.99,1000),
    Dish("chocoloate ice cream",1.99,300),
    Dish("vanilla ice cream",1.99,300),
    Dish("instant noodle",1.99,400),
    Dish("subway sandwich",7.99,750),
    Dish("dumpling",0.99,50),
    Dish("sushi",3.99,350),
    Dish("fried chicken",4.49,650)
    ]

def Dishlist_change_price_keep_list(d: list, p: float):
    for i in range(len(d)):
        d[i] = (Dish_change_price(d[i], p))
        

def before_after():
    #global DL3
    pc=float(input('How much change?'))
    print(Dishlist_display(DL3))
    Dishlist_change_price_keep_list(DL3, pc)
    print(Dishlist_display(DL3))

before_after()

#part e
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
#e.1
print("---Part e.1--")
print("")
M1=[
    Dish("escargots",12.95,250),
    Dish("poached salmon",18.50,550),
    Dish("rack of lamb",24.00,850)
    ]
R1=Restaurant("Pascal","French","940-752-0107",M1)
#e.2
print("---Part e.2--")
print("")
def Restaurant_first_dish_name(r:Restaurant)->str:
    return r.menu[0].name
assert (Restaurant_first_dish_name(R1)) == 'escargots'
#e.3
print("---Part e.3--")
print("")
def Restaurant_is_cheap(r:Restaurant,n:float)->bool:
    return Dishlist_average(r.menu)<=n
assert Restaurant_is_cheap(R1,50)==True
#e.4
print("---Part e.4--")
print("")
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])
c1=[R1,r1,r2]

import copy
def Collection_raise_prices(c:list)->list:
    result=copy.deepcopy(c)
    for i in result:
        for a in range(len(i.menu)):
            i.menu[a] = (Dish(i.menu[a].name,i.menu[a].price+2.50,i.menu[a].cal))
    return result
assert Collection_raise_prices(c1)==[Restaurant(name='Pascal', cuisine='French', phone='940-752-0107', menu=[Dish(name='escargots', price=15.45, cal=250), Dish(name='poached salmon', price=21.0, cal=550), Dish(name='rack of lamb', price=26.5, cal=850)]), Restaurant(name='Thai Dishes', cuisine='Thai', phone='334-4433', menu=[Dish(name='Mee Krob', price=15.0, cal=500), Dish(name='Larb Gai', price=13.5, cal=450)]), Restaurant(name='Taillevent', cuisine='French', phone='01-44-95-15-01', menu=[Dish(name='Homard Bleu', price=47.5, cal=750), Dish(name='Tournedos Rossini', price=67.5, cal=950), Dish(name="Selle d'Agneau", price=62.5, cal=850)])]
def Collection_change_prices(c:list,p:float)->list:
    result=copy.deepcopy(c)

    for i in result:
        Dishlist_change_price_keep_list(i.menu,p)
    return result
assert Collection_change_prices(c1,100)==[Restaurant(name='Pascal', cuisine='French', phone='940-752-0107', menu=[Dish(name='escargots', price=25.9, cal=250), Dish(name='poached salmon', price=37.0, cal=550), Dish(name='rack of lamb', price=48.0, cal=850)]), Restaurant(name='Thai Dishes', cuisine='Thai', phone='334-4433', menu=[Dish(name='Mee Krob', price=25.0, cal=500), Dish(name='Larb Gai', price=22.0, cal=450)]), Restaurant(name='Taillevent', cuisine='French', phone='01-44-95-15-01', menu=[Dish(name='Homard Bleu', price=90.0, cal=750), Dish(name='Tournedos Rossini', price=130.0, cal=950), Dish(name="Selle d'Agneau", price=120.0, cal=850)])]
#e.5
print("---Part e.5--")
print("")
def Colllection_select_cheap (c:list,n:float)->list:
    result=[]
    for i in c:
        if Dishlist_average(i.menu)<=n:
            result.append(i)
    return result
assert Colllection_select_cheap(c1,15)==[Restaurant(name='Thai Dishes', cuisine='Thai', phone='334-4433', menu=[Dish(name='Mee Krob', price=12.5, cal=500), Dish(name='Larb Gai', price=11.0, cal=450)])]

#g
print("---Part g--")
print("")
#4.13.a
print("---Partg 4.13.a--")
print("")
s='abcdefghijklmnopqrstuvwxyz'
print(s[1:3])
print("---Partg 4.13.b--")
print("")
#b
print(s[0:14])
print("---Partg 4.13.c--")
print("")
#c
print(s[14:])
#d
print("---Partg 4.13.d--")
print("")
print(s[1:-1])
#4.14.a
print("---Partg 4.14.a--")
print("")
log='128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"'
#b
print("---Partg 4.14.b--")
print("")
address=log.split(' ')
address=address[0]
print(address)
#c
print("---Partg 4.14.c--")
print("")
date=log[log.find('['):log.find(']')+1]
print(date)
#4.19
print("---Part g 4.19--")
print("")
first='Marlena'
last='Sigel'
middle='Mae'
#a
print("---Part g 4.19.a--")
print("")
print(last+', '+first,middle)
#b
print("---Part g 4.19.b--")
print("")
print(last+', '+first,middle[0]+'.')
#c
print("---Part g 4.19.c--")
print("")
print(first,middle[0]+'.',last)
#d
print("---Part g 4.19.d--")
print("")
print(first[0]+'.',middle[0]+'.',last)

#4.23
print("---Part g 4.23--")
print("")
def average()->float:
    result=0.0
    sentence=input("Enter a sentence:")
    sentence=sentence.split()
    print(sentence)
    for i in sentence:
        result+=len(i)
    return result/len(sentence)

#h
print("---Part h--")
print("")
Count = namedtuple("Count", "letter number")

def one_letter_count(a:str,b:str)->Count:
    counter=0
    for i in a:
        if i in b:
            counter+=1
    return Count(b,counter)
    
def letter_count(a: str, b: str) -> list:
    result = []
    for i in b:
        result.append(one_letter_count(a, i))
    return result

