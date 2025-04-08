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
# from tokenize import blank_re

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

user_input = ["bacil", "cilba", "bilca"]

list_a = ["a", "b", "c"]
list_b = ["i", "l"]

wait_time = 0    # result

count_1 = 0
count_2 = 0
repeated = []

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

# test_st_kandidatov = 5
# test_histogram = [1, 2, 1, 3, 1, 4, 2, 1, 4, 4, 1, 2, 1, 3, 3, 2, 4, 1, 1, 1, 2, 2, 2, 3, 3, 4, 1, 1, 1, 2, 2, 2, 3, 3, 4, 1, 1, 1, 2, 2, 2, 3, 3, 4, 1, 1, 1, 2, 2, 2, 3, 3, 4]

import matplotlib.pyplot as plt

plt.hist(test_histogram)
plt.show()

rezultati = [[] for k in range(1, test_st_kandidatov)]

l = 0
while l < len(test_histogram):
    for m in test_histogram:
        rezultati[l].append("*")
        l += 1

print(rezultati[0])

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

test_glasovi = [1, 3, 2, 4, 1, 4, 7, 6, 1, 2]
test_length = len(test_glasovi)
# print(test_length, type(test_length))
test_results = list(range(len(test_glasovi)))
# print(test_results, "test print")
test_results2 = [None] * test_length
# print("test print", test_results2)
# def test_arrangements():
test_results3 = []
c = 0
for b in test_glasovi:
    test_results3.append(str(c+1)+':')
    c += 1

    for d in test_results3:
        d = str(d)
        d = d + :
print("test print 3 - number of votes", test_results3)
test_kandidati = 7
test_results4 = [f"{e+1}:" for e in range(test_kandidati)]    # range sem sam dodal, ostalo skopiral od nekod
print("test print 4 - variation of votes", test_results4)

g = 0
while g < len(test_glasovi):
    for h in test_glasovi:
        test_results4 = [f"{test_results4[h-1]}" + "*" for h in test_glasovi]

    g +=1
i = 0
k = 0
while i < test_kandidati:
    print("test print 5", test_results4[k])
    i += 1
    k += 1

print("test print 4", test_results4)

# for a in test_glasovi:

    #test_results2.insert(a, '*')
# print("test print where we are", test_results2)

test_candidates = 7
#test_votes_counter = {}
#while len(votes_counter) < candidates:
#    keys = [f"{l+1}:" for l in range(candidates)]
#    values =
#test_votes_counter2 = dict.fromkeys(test_results4)
#print("test print dict votes counter", votes_counter2)

test_results5 = [e+1 for e in range(test_candidates)]
print("test results 5:", test_results5)
test_votes_counter3 = dict.fromkeys(test_results5, str())
print("test votes counter 3", test_votes_counter3)    # yay it works, so far so good

for m in test_glasovi:
    test_votes_counter3[m] = test_votes_counter3[m] + str('*')

print("test print final??:", test_votes_counter3)

for n in test_votes_counter3:
    print(n, ":", test_votes_counter3[n])
"""
# all of test code commented in so I can use this file again for testing in the future.

#f = open("example.txt", "r")
#print(f.readline())
#for x in f:
#  print(x)
#f.close()
"""
test_dict = {"Luka" : 5, "Matija" : 2, "Urša" : 1, "Leopold" : 3, "Karla" : 4}
sorted_test_dict = dict(sorted(test_dict.items(), key=lambda item: item[1], reverse=False))
print(sorted_test_dict)    # okay this works now finally yay big happy
"""
###

test_file = open("example.txt", "r")
test_index = 0
test_existing_billboard = []
while test_index < 10:
    test_existing_billboard.append(test_file.readline())
    test_index += 1
print("wat?", test_existing_billboard)    # lets see what we are working with
print("lets se ewhat we are working with:", type(test_existing_billboard))


"""
test_ind = 0
test_billboard = {}
while test_ind < 10:
    for test_entry in test_existing_billboard:
        test_name_var, test_result_var, *test_rank_var = map(str, test_existing_billboard.split(" "))
        # result_var = int(result_var)    #would maybe work without this line and declaring integer in the next line???
        test_billboard[test_name_var] = test_result_var
    test_ind += 1
"""
#print(test_billboard)
test_file.close()
