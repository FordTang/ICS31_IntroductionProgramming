# William Allison 92486388 and Ford Tang 46564602 ICS 31 Lab sec. 8.  Lab asst. 4

print ("----- (c) -----")
print()
print('Exercise 3.17')

a,b,c=3,4,5
if a<b:
    print ('OK')

if c<b:
    print ('OK')

if a+b == c:
    print ('OK')

if a**2 + b**2 == c**2:
    print ('OK')

print()
print('Exercise 3.18')

if a<b:
    print ('OK')
else:
    print('Not OK')

if c<b:
    print ('OK')
else:
    print('Not OK')

if a+b == c:
    print ('OK')
else:
    print('Not OK')

if a**2 + b**2 == c**2:
    print ('OK')
else:
    print('Not OK')

print()
print('Exercise 3.19')

lst = ['January','February','March']

for i in lst:
    print(i[0:3])

print()
print('Exercise 3.20')

lst =  [2,3,4,5,6,7,8,9]

for i in lst:
    if i**2%8 == 0:
        print(i)

print()
print('(d.1)')
print()

def is_vowel(x:str) -> bool:
    #Checks if input is a vowel
    return(x.upper() == 'A' or x.upper() =='E' or x.upper() =='I' or
           x.upper() =='O' or x.upper() =='U')
assert is_vowel('o') == True
assert is_vowel('k') == False

print()
print('(d.2)')
print()

def print_nonvowels(var:str):
    #prints all non-vowel characters of a string
    for i in var:
        if is_vowel(i) == False:
            print(i)


print()
print('(d.3)')
print()

def nonvowels(var:str) -> str:
    #returns all non-vowel characters of a string
    result = ''
    for i in var:
        if is_vowel(i) == False:
            result+= i
    return result
assert nonvowels('variable') == 'vrbl'

print()
print('(d.4)')
print()

def consonants(var = str)->str:
    #returns all consonant characters of a string in a string
    result = ''
    for i in var:
        if 'A'<=i<='z':
            if is_vowel(i) == False:
                result+= i
    return result
assert(consonants('hruioel543io2()') == 'hrl')
        
print()
print('(d.5)')
print()

def select_letters(choice:str,var:str)->str:
       # returns consonants if first argument is c and vowels if same is v
       result = ''
       if choice.lower() =='v':
           for i in var:
               if 'A'<=i<='z':
                   if is_vowel(i) == True:
                       result+= i
           return result
       elif choice.lower() == 'c':
           return(consonants(var))
       else:
           return ('')
assert (select_letters('v', 'variable') == 'aiae')
assert (select_letters('c', 'variable') == 'vrbl')
assert (select_letters('f','var') == '')

print()
print('(d.6)')
print()

def hide_vowels(var:str)->str:
    #returns input with all vowels replaced by '-'
    result = ''
    for i in var:
        if is_vowel(i) == True:
            result+= '-'
        else:
            result+= i
    return result
assert (hide_vowels('The quick brown fox is too much to type') == 'Th- q--ck br-wn f-x -s t-- m-ch t- typ-')

print()
print('(e)')
print()

print()
print('Exercise 3.23')
print()

lst = []
result = ''
other = 0
var = input('Enter list: ')
for i in var:
    if i == ',':
        lst.append(result)
        result = ''
    elif i == ' ':
        result = result
    else:
        result+=i
lst.append(result)

for i in lst:
    if 'A'<=i[0].upper()<='M':
        print(i)

print()
print('Exercise 3.24')
print()

lst = []
result = ''
other = 0
var = input('Enter list: ')
for i in var:
    if i == ',':
        lst.append(result)
        result = ''
    elif i == ' ':
        result = result
    else:
        result+=i
lst.append(result)
print (lst[0])
print (lst[-1])

print()
print('(f)')
print()

from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]




print()
print('(f.1)')
print()

def alphabetical(varlist:list)->list:
    #sorts alphabetically
    return varlist.sort()

print()
print('(f.2)')
print()

def alphabetical_names(varlist:list)->list:
    #Returns list of names sorted alphabetically
    newlist = sorted(varlist)
    result = []
    for i in newlist:
        result.append(i.name)
    return result
        
print()
print('(f.3)')
print()

def all_Thai(varlist:list)->list:
    #Returns list of restaurants with Thai attributes
    resultlist = []
    for i in varlist:
        if i.cuisine == 'Thai':
            resultlist.append(i)
    return resultlist
assert (all_Thai(RL) == [Restaurant(name='Thai Touch', cuisine='Thai', phone='444-3333', dish='Mee Krob', price=10.95), Restaurant(name='Thai Dishes', cuisine='Thai', phone='333-4433', dish='Paht Woon Sen', price=8.5), Restaurant(name='Thai Spoon', cuisine='Thai', phone='334-3344', dish='Mussamun', price=9.0), Restaurant(name='Jitlada', cuisine='Thai', phone='324-4433', dish='Paht Woon Sen', price=15.5)])

print()
print('(f.4)')
print()

def select_cuisine(cuisine:str,varlist:list)->list:
    #Returns list with user-defined attribute
    resultlist = []
    for i in varlist:
        if i.cuisine == cuisine:
            resultlist.append(i)
    return resultlist

print()
print('(f.5)')
print()

def select_cheaper(maxvar:float,varlist:list)->list:
    #returns list of restaurants with a price less than that given
    resultlist = []
    for i in varlist:
        if i.price <= maxvar:
            resultlist.append(i)
    return resultlist

print()
print('(f.6)')
print()

def average_price(varlist:list)->float:
    sumvar = 0
    for i in varlist:
        sumvar+=i.price
    return sumvar / len(varlist)

print()
print('(f.7)')
print()

print('Average price of all Thai restaurants: ',average_price(all_Thai(RL)))

print()
print('(f.8)')
print()

print('Average price of all Thai and Chinese restaurants: ', (average_price(all_Thai(RL)) + average_price(select_cuisine('Chinese',RL)))/2)

print()
print('(f.9)')
print()

print(alphabetical_names(select_cheaper(15,RL)))

print()
print('(g)')
print()
print('(Exercise 3.25)')
print()

n=int(input('Enter n: '))
for i in range(4):
    print(n*i)

print()
print('(Exercise 3.26)')
print()

n=int(input ('Enter n: '))
for i in range(n):
    print(i**2)

    
