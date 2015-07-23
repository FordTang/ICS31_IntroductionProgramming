# Ford Tang 46564602 and Andrea Castellanos 93578193.  ICS 31 Lab Sec 8.  Lab Asst 2.

#c: 
hours = int(input('How many hours?  '))
print ('This many hours:', hours)
rate = int(input('How many dollars per hours?  '))
print ('This many dollars per hour:  $', rate)
print ('Weekly salary:  $', hours * rate)


#c.1:
name = input('Hello.  What is your name?  ')
print ('Hello, ', name)
print ("It's nice to meet you.")
age = int(input('How old are you?  '))
print ('Next year you will be ', age + 1, ' years old.')
print ('Good-bye!')


#d: 
KRONE_PER_EURO = 7.46
KRONE_PER_POUND = 8.81
KRONE_PER_DOLLAR = 5.5

print ('Please provide this information: ')
business_name = input('Business name: ')
euros = int(input('Number of euros: '))
pounds = int(input('Number of pounds: '))
dollars = int(input('Number of dollars: '))

print ('Copenhangen Chamber of Commerce')
print ('Business name: ', business_name)
print (euros, 'Euros is', euros * KRONE_PER_EURO, 'krone')
print (pounds, 'Pounds is', pounds * KRONE_PER_POUND, 'krone')
print (dollars, 'Dollars is', dollars * KRONE_PER_DOLLAR, 'krone')

print ('Total krone:', (euros * KRONE_PER_EURO) + (pounds * KRONE_PER_POUND) + (dollars * KRONE_PER_DOLLAR))


#e: 
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes', 'Arthur Conan Doyle', 1905, 25.00)

#e.2
print ('The title of still_another is: ', still_another[0])
#e.3
print ('The price of Memoirs of Sherlock Holmes is:  $', another[3])
#e.3
print ('The average price of all three books is:  $', (favorite[3] + another[3] + still_another[3]) / 3)
#e.4
print ('Was ', favorite[0], ' published before 1900?:  ', favorite[2] < 1900)
#e.5
still_another = Book('Return of Sherlock Holmes', 'Arthur Conan Doyle', 1905, 26.00)
print ('The price for ', still_another[0], ' is now:  $', still_another[3])
#e.6
still_another = Book('Return of Sherlock Holmes', 'Arthur Conan Doyle', 1905, 26.00 * 1.2)
print ('The price for ', still_another[0], ' has increased by 20% and is now:  $', still_another[3])


#f
from collections import namedtuple
animal = namedtuple('animal', 'name species age weight favorite_food')
i = animal('Jumbo', 'elephant', 50, 1000, 'peanuts')
ii = animal('Perry', 'platypus', 7, 1.7, 'shrimp')
print ('Does', i[0], 'weigh less than', ii[0], '?  ', i[2] < ii[2])


#g
booklist = [favorite, another, still_another]
#g.1
print ('Is', booklist[0].title, 'cheaper than', booklist[1].title, '?', booklist[0].price < booklist [1].price) 
#g.2
print ('Was', booklist[0].title, 'published later than', booklist[-1].title, '?', booklist[0].year > booklist[-1].year)

#h
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
#h.1
print (RC[2].name)
#h.2
print ('Do', RC[0].name, 'and', RC[3].name, 'share the same food?', RC[0].cuisine == RC[3].cuisine)
#h.3
print ('The price of', RC[-1].dish, 'is $', RC[-1].price)
#h.4
RC.sort()
print (RC)
#h.5
print (RC[-1].dish)
#h.6
RC2 = [RC[0], RC[1], RC[-2], RC[-1]]
print (RC2)


#i
#2.26
import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
s.exitonclick()

#2.27
import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.right(45)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
s.exitonclick()

#2.28
import turtle
s = turtle.Screen()
t = turtle.Turtle()
sides = 72
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
s.exitonclick()

import turtle
s = turtle.Screen()
t = turtle.Turtle()
sides = 60
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
s.exitonclick()

import turtle
s = turtle.Screen()
t = turtle.Turtle()
sides = (180 - (900/7))
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
s.exitonclick()

import turtle
s = turtle.Screen()
t = turtle.Turtle()
sides = 45
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
t.left(sides)
t.forward(100)
s.exitonclick()


#2.29
import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.circle(100)
t.penup()
t.forward(50)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()
t.circle(100)
t.penup()
t.left(180)
t.forward(100)
t.left(180)
t.pendown()
t.circle(100)
s.exitonclick()


#2.32
import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.circle(109)
t.penup()
t.forward(150)
t.pendown()
t.circle(1)
s.exitonclick()


#j
import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.right(180)
t.circle(500,35)
t.left(110)
t.circle(500,35)
t.circle(500,35)
t.left(110)
t.circle(500,35)
t.circle(91)
t.penup()
t.left(90)
t.forward(91)
t.right(90)
t.dot(50, 'black')
s.exitonclick()

