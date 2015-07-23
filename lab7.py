#  Wenqi Li 20112696 and Ford Tang 46564602.  ICS 31 Lab sec 7.  Lab asst 7.

print('--------part c----------')
print()
print('part c1')
from random import randrange
infile = open('surnames.txt', 'r')
temp = infile.readlines()
surnames = []

for i in temp:
    listString = i.split()
    surnames.append(listString[0][0] + listString[0][1:].lower())
infile.close()

infile = open('femalenames.txt', 'r')
temp = infile.readlines()
female_names =[]

for i in temp:
    listString = i.split()
    female_names.append(listString[0][0] + listString[0][1:].lower())
infile.close()

infile = open('malenames.txt', 'r')
temp = infile.readlines()
male_names =[]

for i in temp:
    listString = i.split()
    male_names.append(listString[0][0] + listString[0][1:].lower())
infile.close()

'''
def random_names(i:int) ->list:
    infile = open('surnames.txt', 'r')
    result= eval(infile.read())
    for i in result:
        
    return
'''

def random_names(number:int) -> [str]:
    result = []
    for i in range(number):
        result.append(single_random_name())
    return result

def single_random_name() -> str:
    result = ''
    
    result += random_name_from_list(surnames) + ', '
    if randrange(0,2) == 0:
        result += random_name_from_list(female_names)
    else:
        result += random_name_from_list(male_names)
    
    return result        

def random_name_from_list(lst:[str]) -> str:
    return lst[randrange(0,len(lst))]
print('---------------part d-----------------')
print()
print()
ALPHABET2 = 'abcdefghijklmnopqrstuvwxyz'

def rotate_alphabet(numb2: int)->str:
    temp = ((ALPHABET2 + ALPHABET2[:numb2%26]))
    return temp

   
def Caesar_encrypt(s: str, numb: int):
    temp = rotate_alphabet(numb)
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', temp[numb%26:])
    return s.translate(table)

print(Caesar_encrypt('hello my name is bobz', 31))

def Caesar_decrypt(d: str, numb2: int):
    temp = rotate_alphabet(numb2)
    table = str.maketrans(temp[numb2%26:], 'abcdefghijklmnopqrstuvwxyz')
    return d.translate(table)

print(Caesar_decrypt(Caesar_encrypt('hello my name is bobz', 5), 5))

def strip_punctuation(word:str)->str:
    result=""
    punctuation = ",.?!:;-()_[]/{}<> "
    for i in word:
        if i not in punctuation:
            result += i
    return result
assert strip_punctuation("abc.,'[] abc") == "abc'abc"

infile = open('wordlist.txt')
dictionary = infile.read()
infile.close()

def Caesar_break(cipher:str) -> str:
    temp = cipher.split()
    for i in range(len(temp)):
        temp[i] = strip_punctuation(temp[i])
    top_count = 0
    match = 0

    for i in range(26):
        count = 0
        for n in temp:
            if Caesar_decrypt(n, i) in dictionary:
                count+=1
        if count >= top_count:
            top_count = count
            match = i
    return Caesar_decrypt(cipher, match)
print('---------------part d.2-----------------')
print()
print()
def Caesar_break(cipher:str) -> str:
    temp = cipher.split()
    for i in range(len(temp)):
        temp[i] = strip_punctuation(temp[i])
    top_count = 0
    match = 0

    for i in range(26):
        count = 0
        for n in temp:
            if Caesar_decrypt(n, i) in dictionary:
                count+=1
        if count >= top_count:
            top_count = count
            match = i
    return Caesar_decrypt(cipher, match)
print(Caesar_break('mjqqt rd sfrj nx gtge'))

print('---------------part e-----------------')
print()
print()
print('---------------part e.1-----------------')
print()
print() 
def copy_file():
  infile_name = input("Please enter the name of the file to copy: ")
  infile = open(infile_name, 'r')
  outfile_name = input("Please enter the name of the new copy:  ")
  outfile = open(outfile_name, 'w')
  for line in infile:
      outfile.write(line)
  infile.close()
  outfile.close()


print('---------------part e.2-----------------')
print()
print() 

def copy_file(line_numbers: str ):
  infile_name = input("Please enter the name of the file to copy: ")
  infile = open(infile_name, 'r')
  outfile_name = input("Please enter the name of the new copy:  ")
  outfile = open(outfile_name, 'w')
  if line_numbers == 'line numbers':
      count = 0
      for line in infile:
          count+=1
          line2 = ("{:5d}: {:}".format(count, line))
          outfile.write(line2)
        
  else:
      for line in infile:
        outfile.write(line)
  infile.close()
  outfile.close()

print('---------------part e.3-----------------')
print()
print() 



def copy_file(trim: str ):
  infile_name = input("Please enter the name of the file to copy: ")
  infile = open(infile_name, 'r')
  outfile_name = input("Please enter the name of the new copy:  ")
  outfile = open(outfile_name, 'w')
  if trim == 'Gutenberg trim':
      ignore = True
      for line in infile:
          if "*** START" in line:
              ignore = False
          if "*** END" in line:
              outfile.write(line)
              break
          if ignore is False:
                outfile.write(line)        
  else:
      for line in infile:
        outfile.write(line)
  infile.close()
  outfile.close()


print('---------------part e.4-----------------')
print()
print() 
def stats(lst: [str]) -> str:
    #Prints strings in a formatted output
    result =''
    result += "{0:5}    {1:}".format(len(lst), "lines in the list") + '\n'
    result += "{0:5}    {1:}".format(lst.count('\n'), "empty lines") + '\n'
    
    num = 0
    for i in lst:
        num += len(i)
    average_chars = num / len(lst)
    average_chars_nonempty = num / (len(lst) - lst.count('\n'))
    
    result += "{0:8.2f} {1:}".format(average_chars, "average characters per line") + '\n'
    result += "{0:8.2f} {1:}".format(average_chars_nonempty, "average characters per non-empty line")
    return result

def copy_file(Stats:str):
  infile_name = input("Please enter the name of the file to copy: ")
  infile = open(infile_name, 'r')
  outfile_name = input("Please enter the name of the new copy:  ")
  outfile = open(outfile_name, 'w')
##  filelist = infile.readlines()
  if Stats == 'statistics':
      statfile = open(infile_name, 'r')
      filelist = statfile.readlines()
      for line in infile:
          outfile.write(line)
      print(stats(filelist))
  else:
      for line in infile:
        outfile.write(line)
  infile.close()
  outfile.close()




























