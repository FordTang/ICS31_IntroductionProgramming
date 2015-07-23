#  Ford Tang 46564602 and Michael Ragheb 66786623.  ICS 31 Lab sec 8.  Lab asst 6.
from random import randrange

# C

print('\n**C.1**')

for i in range(50):
    print(str(i+1) + ". " + str(randrange(0, 11)))

# c.2
print('\n**C.2**')

def roll2dice() -> int:
    #Functions returns a number that reflects the random roll of 2 dice
    return (randrange(1,7) + randrange(1,7))

 
for i in range(50):
    print (roll2dice())


# c.3
print('\n**C.3**')

def distribution_of_rolls(num_of_rolls: int) -> str:
    ''' Returns output of the distribution of the values of two dice rolls
    '''
    lst = []
    for i in range(num_of_rolls):
        lst.append(roll2dice())

    output = ''
    for i in range(2, 13):
        count_of_occurences = lst.count(i)
        output += str(i) + ':\t' + str(count_of_occurences) + ' (' + str(round((count_of_occurences/num_of_rolls) * 100, 2)) + '%)\t' + ('*' * count_of_occurences) + '\n'
    output += "-----------------------\n\t" + str(num_of_rolls) + " rolls"
    return output

print(distribution_of_rolls(200))

# d
print('\n**d**')

# d.1
print('\n**d.1**')

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate_alphabet(number:int) -> str:
    if number > 26:
        number = number % 26
    return (ALPHABET[number:] + ALPHABET[:number])

def Caesar_encrypt(message:str, key:int) -> str:
    # Function encrypts a message with an integer key
    table = str.maketrans(ALPHABET, rotate_alphabet(key))
    return (message.lower().translate(table))

def Caesar_decrypt(message:str, key:int) -> str:
    # Function decrypts a message with an integer key
    table = str.maketrans(rotate_alphabet(key), ALPHABET)
    return(message.lower().translate(table))

assert Caesar_encrypt("How are you doing?", 5) == 'mtb fwj dtz itnsl?'
assert Caesar_decrypt("mtb fwj dtz itnsl?", 5) == "how are you doing?"

# d.2
print('\n**d.2**')


#d.3
print('\n**d.3**')
print("We did it.")

#e
print('\n**e**')

#e.1
print('\n**e.1**')

example = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]
def print_line_numbers(lst:list):
    for i in range(len(lst)):
        print ('{0:5}{1:}'.format(str(i+1)+':',str(lst[i])))

####### DO E.2 AND E.3 !!!!!!!!!!!######################
#e.2
print('\n**e.2**')

def stats(lst: [str]) -> None:
    #Prints strings in a formatted output
    print("{0:5}    {1:}".format(len(lst), "lines in the list"))
    print("{0:5}    {1:}".format(lst.count(''), "empty lines"))

    num = 0
    for i in lst:
        num += len(i)
    average_chars = num / len(lst)
    average_chars_nonempty = num / (len(lst) - lst.count('\n\n'))
    
    print("{0:8.2f} {1:}".format(average_chars, "average characters per line"))
    print("{0:8.2f} {1:}".format(average_chars_nonempty, "average characters per non-empty line"))

#e.3
print('\n**e.3**')

def strip_punctuation(word:str)->str:
    result=""
    punctuation = ",.?!:;-()_[]/{}<> "
    for i in word:
        if i not in punctuation:
            result += i
    return result
assert strip_punctuation("abc.,'[] abc") == "abc'abc"

        
def list_of_words(lst:[str])->list:
    result = []
    for i in lst:
        result.append(strip_punctuation(i))
    return result
assert list_of_words(example) == ['Fourscoreandsevenyearsagoourfathersbroughtforthon', 'thiscontinentanewnationconceivedinlibertyanddedicated', 'tothepropositionthatallmenarecreatedequalNowweare', 'engagedinagreat\t\tcivilwartestingwhetherthatnationorany', 'nationsoconceivedandsodedicatedcanlongendure']

#f
print('\n**f**')
