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
txt = "single quote", " \\backslash", "Hello \nChat \n new line", " \r carriage return", " \n \t tab",
" backspace \b", " \f form feed" #\ooo octal value, \xhh hex value; \n lets see how this prints"     #this doesnt work yet
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
