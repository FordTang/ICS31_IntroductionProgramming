# Sean Woong 70753892 and Ford Tang 46564602 ICS 31 Lab 8. Lab asst. 3

#
#
# Part (c)
#
#
print('')
print('')
print('------Part C -------')
print('')
print('')
#
# 3.36
#
def abbrevation(x:str)->str:
    '''
    return first two letters
    '''
    return x[0] + x[1]

assert abbrevation('Tuesday')== 'Tu'
assert abbrevation('Wednesday')== 'We'
assert abbrevation('Sunday')== 'Su'

print(abbrevation ('Tuesday'))
print ('')

#
#3.43
#
def distance(x:float)->float:
    '''
    returns the distance of a lightning strike in kilometers
    '''
    return x * (340.29/1000)

print(distance(6))
print(distance(3))

assert distance(6)== 2.0417400000000003

print ('')

#
#3.35
#

def points(x1:int, x2:int) -> int:
    '''
    returns the distance between points x1 and x2
    '''
    return x2 - x1

assert points (2,1) == -1
assert points (1,2) == 1

x1 = int(input('Please enter a value for the first point:  '))
x2 = int(input('Please enter a value for the second point:  '))
print ('The distance from point x2 to x1 is ', points(x1, x2))

print ('')

#
#3.44
#

import turtle
s = turtle.Screen()
t = turtle.Turtle()

def polygon(sides: int) -> int:
    turn = (180 - (180 * (sides-2))/sides)
    for i in range(sides):
        t.forward(100)
        t.left(turn)
    return 0

polygon(4)
s.exitonclick()

print ('')
#
#
# Part (d)
#
#
print('')
print('')
print('------Part D -------')
print('')
print('')
#
# 3.32
#
def pay(wage:float, hours:float) -> float:
    '''
    returns on employee's pay plus overtime
    '''
    if hours >= 40:
        overtime = hours - 40
    return ((hours - overtime) * wage) + (overtime*(wage*1.5))

assert pay(10,41) == 415.0
assert pay(10,40) == 400.0
print(pay(10,41))
print ('')
#
#
# Part (e)
#
#
print('')
print('')
print('------Part E -------')
print('')
print('')

from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

def restaurant_price(price:Restaurant)-> float:
    '''
    returns the price of a restaurant
    '''
    return price.price
assert restaurant_price(RC[0])== 12.5
assert restaurant_price(RC[1])== 5.5
assert restaurant_price(RC[-1])== 10.5

print('Dish price for',RC[0].name, 'is: ',restaurant_price(RC[0]))
print('Dish price for',RC[1].name, 'is: ',restaurant_price(RC[1]))
print('Dish price for',RC[-1].name, 'is: ',restaurant_price(RC[-1]))

print('')

print('Restaurants sorted by price:\n')
RC.sort(key=restaurant_price)
print(RC)

def costliest(restaurants:list) -> str:
    most_expensive = restaurants[0].price
    most_name = restaurants[0].name
    for i in range(len(restaurants)):
        if restaurants[i].price > most_expensive:
            most_expensive = restaurants[i].price
            most_name = restaurants[i].name
    return most_name
assert costliest(RC) == 'Noma'

print ('\nThe most expensive restaurant is: ',costliest(RC))
print('')
print('')
print('------Part F -------')
print('')
print('')
from collections import namedtuple
Book = namedtuple('Book', 'author title genre year price instock')
BSI = [
    Book('John Appleseed', 'Intro to Programming', 'Textbook', 2008, 59.50, 100),
    Book('Bruce Wayne', 'Under the Red Hood', 'Comics', 2010, 14.99, 70),
    Book('Sam Liu', 'Chinese Cooking 101', 'Cookbook', 2011, 29.50, 200),
    Book('Max Schneider', 'The Struggle: The Max Schneider Story', 'Biography', 2013, 18.50, 125),
    Book('Bartholomew Allen', 'Justice League: Flashpoint Paradox', 'Comic', 2013, 16.50, 140),
    Book('Oscar Wilde', 'The Picture of Dorian Gray', 'Fiction', 1859, 12.99 , 80) ]

#F.1
for i in BSI:
    print(i.title)

print('')
print('')
print('')
print('')
#F.2

def return_title(title:Book) -> str:
    return (title.title)
assert return_title(BSI[0]) == 'Intro to Programming'

BSI_copy = BSI.copy()

BSI_copy.sort(key=return_title)

for i in BSI_copy:
    print(i.title)
#F.3
print('')
print('')
print('')
print('')

for i in range(len(BSI)):
    BSI[i] = BSI[i]._replace(price = BSI[i].price * 1.1)

print (BSI)
#F.4
print('')
print('')
print('')
print('')
for i in range(len(BSI)):
    BSI[i] = BSI[i]._replace(genre = 'Technology')

print(BSI)

#F.5
print('')
print('')
print('')

BSI_old = []
BSI_new = []

for i in BSI:
    if i.year < 2000:
        BSI_old.append(i)
    else:
        BSI_new.append(i)

print (BSI_old)
print("")
print (BSI_new)

if len(BSI_old) > len(BSI_new):
    print ('More books before 2000')
    print (len(BSI_old)), '>', (len(BSI_new))
else:
    print ('More books after 2000')
    print ((len(BSI_new)), '>', (len(BSI_old)))

#F.6
print('')
print('')
print('')


def inventory_value(instock:Book) -> float:
    return (instock.instock * instock.price)
assert inventory_value(BSI[0]) == 6545.0
def top_value(instock:list) -> Book:
    highest_value = instock[0].price
    highest_book = instock[0]
    for i in range(len(instock)):
        if instock[i].price > highest_value:
            highest_value = instock[i].price
            highest_book = instock[i]
    return (highest_book)
assert top_value(BSI).title == 'Intro to Programming'
print("The highest value book is", top_value(BSI).title, 'at a value of $', inventory_value(top_value(BSI)))

#
# G
#
print('')
print('')
print('------Part G -------')
print('')
print('')

import turtle
s = turtle.Screen()
t = turtle.Turtle()

t.speed(9)
s.colormode(cmode=255)

#
# Eyes
#

def draw_eye(x: int, y: int):
    "Draws an eye starting from 200 pixels to right.  Takes x, and y coordinates"
    t.penup()
    t.goto(x,y)
    #t.forward(200)
    t.pendown()
    t.dot(90,215, 0,0)
    t.left(180)
    t.penup()
    t.forward(105)
    t.left(180)
    t.right(45)
    t.pendown()
    t.circle(150, 90)
    t.left(90)
    t.circle(150, 90)
    t.left(135)
    t.penup()
    t.forward(105)
    t.pencolor(0,100,150)
    t.pencolor(0,0,0)
    t.forward(105)
    t.left(180)
    t.right(45)
    t.circle(150, 22.5)
    t.right(90)
    t.pendown()
    t.forward(15)
    t.left(180)
    t.forward(15)
    t.right(90)
    t.penup()
    t.circle(150, 22.5)
    t.right(90)
    t.pendown()
    t.forward(15)
    t.left(180)
    t.forward(15)
    t.right(90)
    t.penup()
    t.circle(150, 22.5)
    t.right(90)
    t.pendown()
    t.forward(15)
    t.left(180)
    t.forward(15)
    t.penup()
    t.right(90)
    t.circle(150, 22.5)
    t.left(135)
    t.forward(105)
    t.dot(50, 0,0,0)
    t.penup()

#
# Nose
#

def draw_nose(a: int, b: int):
    t.goto(a, b)
    t.right(125)
    t.pendown()
    t.pensize(5)
    t.forward(125)
    t.right(55)
    t.left(180)
    t.forward(80)
    t.penup()

#
# Mouth
#

def draw_mouth(c: int, d: int):
    t.goto(c,d)    
    t.right(90)
    t.forward(70)
    t.left(90)
    t.forward(85)
    t.left(180)
    t.pendown()
    t.pensize(3)
    t.forward(225)
    t.left(90)
    t.circle(112.5,180)
    t.left(90)
    t.forward(112.5)
    t.pensize(1.5)
    t.left(90)
    t.forward(112.5)
    t.left(180)
    t.forward(112.5)
    t.left(90)
    t.forward(35)
    t.left(90)
    t.forward(107)
    t.left(180)
    t.forward(107)
    t.left(90)
    t.forward(35)
    t.left(90)
    t.forward(90)
    t.left(180)
    t.forward(90)
    t.right(90)
    t.forward(105)
    t.right(90)
    t.forward(107)
    t.right(180)
    t.forward(107)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(90)
    t.right(180)
    t.forward(90)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(56.25)
    t.left(90)
    t.forward(96)
    t.left(180)
    t.forward(192)
    t.penup()
    t.forward(20)
    t.left(90)
    t.forward(80)

def draw_face():
    draw_eye(200, 0)
    draw_eye(-150, 0)
    draw_nose(40, 0)
    draw_mouth(30,-100)

draw_face()

s.exitonclick()
