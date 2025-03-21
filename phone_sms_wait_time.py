import sys

speech = sys.argv[1:]

keys = {" " : 1,
        "a" : 2, "b" : 2, "c" : 2,
        "d" : 3, "e" : 3, "f" : 3,
        "g" : 4, "h" : 4, "i" : 4,
        "j" : 5, "k" : 5, "l" : 5,
        "m" : 6, "n" : 6, "o" : 6,
        "p" : 7, "q" : 7, "r" : 7, "s" : 7,
        "t" : 8, "u" : 8, "v" : 8,
        "w" : 9, "x" : 9, "y" : 9, "z" : 9
}

print("This is the input: ", speech)

key_letters = []
key_list = []

for letters in speech:    # each specific string on its own

    for i in letters:    # each letter of the string from before


        key_list.append([keys[a] for a in i])

key_letters = sum([key_list[z] == key_list[z + 1] for z in range(len(key_list) - 1)])

print("Wait time is: ", key_letters)    # test print to see where we are    #  it is already working wooo hooo
    