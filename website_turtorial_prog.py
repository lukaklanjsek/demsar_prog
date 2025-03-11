print("Hello, world of Python")
import sys
print(sys.version)
#
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x) #why does it print 'awesome' instead of 'fantastic'  #haha figured out its because of local and regional values
#
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
#
x = ("apple", "banana", "cherry")
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))
# return string without any whitespace at the beginning or the end:
txt = " Hello Wrold "
x = txt.strip()
print(x)
# replace char H with J
txt = "Hello world"
txt = txt.replace("H", "J")    # the .replace even suggests you old and new
print(txt)
# correct syntax to add a placeholder for parameter
age = 36
txt = f"My name is John, and I am {age}"  #the trick is to use curly brackets {}
print(txt)
# many values to multiple variables
x, y, z =  "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# unpacking
fruits =  ["Apple", "fruit", "frutis"]
x, y, z = fruits
print(x)
print(y)
print(z)
# print different data types
x = 4
y = "fruits"
print(x, y, z)
# global versus local variables
x = "amazing"
def myfunc():
    x = "specific"
    print("python is " + x)
myfunc()             #why is this myfunc here
print("PYthon is " + x)
#
x = "amazing"
def myfunct():
#    print(x)
    x = 12
    print(x)
#    global x
    x = "specific"
    print(x)
#myfunct()
print("Python is " + x)
# data types
amount = ["abple", "list", 25]  #list
amount2 = ("apple", "banana", 25)     #tuple
print(type(amount))
print(type(amount2))
sdfiuuh = {"name": "John", "address" : "eleven"}    #dictionary
sdfiuuh2 = {"one", "two", "three"}       #set
print(type(sdfiuuh), type(sdfiuuh2))
# type conversion
x = 1
a = float(x)
print(a, type(a))
b = str(a)
print(b, type(b))
# strings
a = """One two three
everybody wants things from me
I am crawled in a baby bed
things look very bad."""
print(a)
print(a[12], len(a))
print(a[17:25], a.upper())
age = {336}
txt = f"My mother is John, how did you {age}"
print(txt)
cost = 11
txt = f"the price is {cost:.2f}"
print(txt)
txt = f"the price keeps increasing {cost + 2}"
print(txt)
# escape character \ + others
txt = "there is an \"escape character\" that allows the double quotations to enter into the print"  # you need to put it in front of every character
print(txt)
# txt = "single quote", " \\backslash", "Hello \nChat \n new line", " \r carriage return", " \n \t tab",
# " backspace \b", " \f form feed" #\ooo octal value, \xhh hex value; \n lets see how this prints"     #this doesnt work yet
print(txt)
txt = "single quotte and \nA new line!"
print(txt)
"""escape_char = (("Code, Result"),
               	Single Quote"),
	Backslash",
	New Line",

	Carriage Return",
	Tab,	Form Feed,
	Octal value",
Hex value),"""
# string methods
# operators here we go again
x = y = z = 10
x /= 3
y %= 3
z //= 3
print(x, y, z)
x = y = z = 15
x &= 7
y |= 8
z ^= 7
print(x, y, z)
# new day new me :)
"""lets try the tripple quote comment:
List is a collection which is ordered and changeable. Allows for duplicates. 
example_list = ["apple", "banana", "cherry"]

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
example_tuple = ("apple", "banana", "cherry")

Set is a collection which is unordered, unchangeable and unindexed. No duplicates.
example_set = {"apple", "banana", "cherry"}

Dictionary is a collection which is ordered and changeable. No duplicates.
example_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1964}"""
#Lists
example_list = ["apple", "banana", "super_smash_bros"]
print(example_list[-1])
example_list += ["lil_chery", "mon_chery", "bon_chery", "das_orange"]
print(example_list[2:])
print(example_list[-3:-1])
if "bon_chery" in example_list:
    print(" Si, si, moin cherry")
example_list[1:3] = ["water_mellon", "seller"]
print(len(example_list))
example_list.insert(5, "MELLON")
example_list.append("reseller")
example_list.insert(2, "Woila")
example_list2 = ["The pope", "the majesty", "the king"]
example_list.extend(example_list2)
example_list3 = ("The boing", "the boeing", "airbus", "supremacy")
example_list.extend(example_list3)
print(example_list)
#non negotiables one two three everybody is after me
example_list += ["airbus", "supremacy"]
example_list.remove("airbus")
print(example_list)
example_list.pop()
del example_list3
example_list2.clear()
i = 0
while i < len(example_list):
    print(example_list[i])
    i += 1
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]    #why is [] needed for printing
newest_list = [x for x in example_list if "c" in x]
print(newest_list)
#new_list = [expression for item in iterable if condition == True]  ...makes a new list leaving the old list unchanged
example_list4 = [x for x in example_list]
example_list5 = [x.upper() for x in example_list]
#print(example_list4)
#print(example_list5)
example_list4.sort(reverse = True)
example_list5.sort()
print(example_list4)
print(example_list5)
#def example_fuction(n):

example_list.sort(key = str.lower)
print(example_list)
# tuples:
example_tuple = ("NUMBAONE",)    #the "," comma makes it a tuple
example_tuple2 = ("NUMBAONE")    #this turns out to become a string
print(type(example_tuple), type(example_tuple2))
example_tuple3 = ("apple", 42, True, "bandana", "cherish", "orange_man")
print(example_tuple3[-3:-1])
test_tuple = ("orange",)
example_tuple3 += test_tuple
(yellow, red, example_red, *test_yellow) = example_tuple3
print(test_yellow, type(test_yellow))
(yellow, *red, green) = example_tuple3
print(yellow, red, green)    #interesting that the tuple still exists, its values were simply extracted or borrowed, not sure yet
for i in range(len(example_tuple3)):
    if i > 2:
        print(example_tuple3[i])    #this worked yay much happy
i = 0
while i < len(example_tuple3):
    print(example_tuple3[i])
    i += 2
example_tuple4 = example_tuple3 * 2
print(example_tuple4)
# python sets, lets {set} an example
# indeed I am very funny
example_set = {"apple", "Banana", "One republic", "one commissairiate", "an example"}
print(example_set)
print(example_set)  #this is still same order of items in a set
example_set1 = {"Apple", "apple", "bannan", True, 1, 2, 3, "apple"}    #set differences the letter capitalisation, so here are as well "Apple" as "apple"
print(example_set1)   #finally a different order of things in a print
print(len(example_set1), len(example_set1), type(example_red), type(example_set1))
example_set.update(example_set1)
print(example_set)
example_set.remove(True)     #i was receiving an error because I forgot and typed " " while attempting to remove the boolean
example_set.discard(1)     #from .remove we will use .discard as supposingly this doesnt throw and error if item already gone
pop_set = {"one", "Two", "three", "everybody", "follow", "me", True}
x = pop_set.pop()    #this truly is random
print(x)
print(pop_set)
set_various = example_set.union(pop_set)
set_various1 = pop_set | example_set
set_ultimate = set_various | set_various1 | pop_set | example_set | example_set1
set_various2 = pop_set.union(example_tuple3)
set_various1.update(set_various2)
print(set_various1)
print(set_ultimate)
set_mega = set_various1.difference(set_ultimate)
set_mega1 = set_various.difference_update(set_various2)
set_oppen = set_various1.symmetric_difference(set_ultimate)
print(set_oppen)
set_ultimate.symmetric_difference_update(set_various1)
print(set_ultimate)
# dictionaries
example_dictionary = {"coffe" : "yes", "type" : "latte", "amount" : "two cups", "Music" : True}
print(example_dictionary)
example_dictionary1 = {"example_key" : "example_value", "Music" : False}
print(len(example_dictionary))
example_dictionary2 = {"brand": "coffe", "value": ["name", "all", "values", "of", "ours"], "colour": True}
print(example_dictionary2)
# New day new opportunity to get the work done
example_dictionary3 = dict(name = "Jacob", age = "proper", country = "Norgay")
print(type(example_dictionary3), example_dictionary3)
x = example_dictionary1.keys()
print(x)
x = example_dictionary.keys()
print(x)  #before change
example_dictionary["coffee"] = "maybe"    # It needed to be a new item and not changing the old key value
print(x)
x = example_dictionary.items()
print(x)
example_dictionary["number"] = "three"
print(example_dictionary)
del example_dictionary["amount"]
print(example_dictionary)
for x in example_dictionary:
    print(x)         #prints keys
for x in example_dictionary:
    print(example_dictionary[x])    #prints values
for x, y in example_dictionary2.items():
    print(x, y)
example_family = {
                  "father" : {"name" : "Jack",
                              "year" : "1974"},
                  "Mother" : {"name" : "Jackie"},
                  "child1" : {
                              "name" : "Josephine",
                              "year" : "2003"},
                  "child2" : {
                              "name" : "Jon",
                              "year" : "2001"},
                  "child3" : {
                              "name" : "Joseph"},
                  }
print(example_family)
