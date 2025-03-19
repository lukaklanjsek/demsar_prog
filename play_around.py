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
"""
import sys
print(sys.version)
# sys.argv = []
print(sys.argv)

the_message = (sys.stdin)

print(the_message, type(the_message))



#for line in sys.stdin:
#    if 'q' == line.rstrip():
#        break
#    print(f'Input : {line}')

print("Exit")
print(sys.argv)

txt = "The best things in life are free!"
print("free" in txt)
"""
user_input = ["bacil", "cilba", "bilca"]

list_a = ["a", "b", "c"]
list_b = ["i", "l"]

wait_time = 0    # result

count_1 = 0
count_2 = 0

def funkcija():

    for i in user_input:
        if i in list_a:
            count_1 += 1
        elif i in list_b:
            count_2 += 1
        i += 1
print(count_1, count_2)

