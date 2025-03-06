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
#