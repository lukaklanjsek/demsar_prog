'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

for e in z:  #why 'e' works???
    print(e)
'''
import sys
print(sys.version)
# sys.argv = []
print(sys.argv)

the_message = list(sys.stdin)

print(the_message, type(the_message))



for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")
print(sys.argv)

txt = "The best things in life are free!"
print("free" in txt)
