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
from exercise_elections import st_kandidatov

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
"""
user_input = ["bacil", "cilba", "bilca"]

list_a = ["a", "b", "c"]
list_b = ["i", "l"]

wait_time = 0    # result

count_1 = 0
count_2 = 0
repeated = []
"""
"""
#def funkcija():
for word in user_input:

    for letter in word:
        #print(i)
        if letter in list_a:
            count_1 += 1    # this is actually not required, just a checkup on test
            repeated.append("test_1")    # test try 1
        elif letter in list_b:
            count_2 += 1    # this is actually not required, it is only of interest if thing works
            repeated.append("test_2")    # try out test
        #letter += 1

test_wait_time = 0
print(repeated)    # i need this check for a test    # this works so far

for number in repeated:
    i = 0
    while i < len(number) -1:    # edited out "-1" # added "-1" again
        if number[i] == number[i + 1]:    # how to fix this line so it would check if two consecutive things are the same  # this is still giving me much troubles  # still troubles
            print("the number counting works correctly")
            test_wait_time += 1

        i += 1
#        else:
#            pass    # editing out "else" part


key_mappings = {
    " ": 1,
    "a": 2,
    "b": 2,
}
test_string = "abba baba"
key_list = [key_mappings[c] for c in test_string]

print(key_list)


#    i +=1    # this one was not needed
print(test_wait_time)

print(wait_time)    # best hopes    # no it does not work yet

print(repeated)    # test so far so good


print(count_1, count_2)

#print(word, i)    # this is no longer needed for a checkup
"""
# test_st_kandidatov = 5
# test_histogram = [1, 2, 1, 3, 1, 4, 2, 1, 4, 4, 1, 2, 1, 3, 3, 2, 4, 1, 1, 1, 2, 2, 2, 3, 3, 4, 1, 1, 1, 2, 2, 2, 3, 3, 4, 1, 1, 1, 2, 2, 2, 3, 3, 4, 1, 1, 1, 2, 2, 2, 3, 3, 4]
"""
import matplotlib.pyplot as plt

plt.hist(test_histogram)
plt.show()
"""
"""
rezultati = [[] for k in range(1, test_st_kandidatov)]

l = 0
while l < len(test_histogram):
    for m in test_histogram:
        rezultati[l].append("*")
        l += 1

print(rezultati[0])
"""
test_value_1 = 15
test_value_2 = 4
test_value_3 = 2
test_value_4 = 0


test_value_2 += test_value_1 // 4
test_value_1 = test_value_1 % 4
test_value_3 += test_value_2 // 3
test_value_2 = test_value_2 % 3
test_value_4 += test_value_3 // 4
test_value_3 = test_value_3 % 3

print(test_value_4, test_value_3, test_value_2, test_value_1)
