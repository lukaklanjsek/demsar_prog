import sys
# speech = sys.argv[1]    # this doesnt work as intended
# print(sys.argv)
speech = sys.argv[1:]
"""
keys = {" " : 1,
        "a" : 2, "b" : 2, "c" : 2,
        "d" : 3, "e" : 3, "f" : 3,
        "g" : 4, "h" : 4, "i" : 4,
        "j" : 5, "k" : 5, "l" : 5,
        "m" : 6, "n" : 6, "o" : 6,
        "p" : 7, "q" : 7, "r" : 7, "s" : 7,
        "t" : 8, "u" : 8, "v" : 8,
        "w" : 9, "x" : 9, "y" : 9, "z" : 9}    # i don't know how to recognise the input " " yet, maybe it will turn out I wouldn't have to worry about space in command line
"""

key_1 = [" "]
key_2 = ["a", "b", "c"]
key_3 = ["d", "e", "f"]
key_4 = ["g", "h", "i"]
key_5 = ["j", "k", "l"]
key_6 = ["m", "n", "o"]
key_7 = ["p", "q", "r", "s"]
key_8 = ["t", "u", "v"]
key_9 = ["w", "x", "y", "z"]

wait_time = 0

def pause_time(speech):
    current_key = ""
    for i in speech:
        if i not in key_1:
            pass
        else:
            current_key = "key_1"
            break
        if i not in key_2:
            pass
        else:
            current_key = "key_2"
            break
        if i not in key_3:
            pass
        else:
            current_key = "key_3"
            break
        if i not in key_4:
            pass
        else:
            current_key = "key_4"
            break
        if i not in key_5:
            pass
        else:
            current_key = "key_5"
            break
        if i not in key_6:
            pass
        else:
            current_key = "key_6"
            break
        if i not in key_7:
            pass
        else:
            current_key = "key_7"
            break
        if i not in key_8:
            pass
        else:
            current_key = "key_8"
            break
        if i not in key_9:
            pass
        else:
            current_key = "key_9"
            break
    if current_key[i] == current_key[i-1]:
        wait_time += 1
    i += 1

print(wait_time)


