import sys

file_name_var = ""    # let's see if we need this
name_var = ""
result_var = 0
rank_var = 0    # high suspicion this does not need to be in the process

#lets make a dictionary with key:value of name_var and result_var
#billboard = dict(__key = name_var , __value = result_var)

#dictionary was a bad idea, in my test area I only got list working
billboard = []

new_line = (sys.argv[1:3])


existing_billboard = open("example.txt", "r")
ind = 0
while ind < 10:
    billboard.append(existing_billboard.readline().split())
    ind += 1

billboard_a = []
billboard_b = []
billboard_c = []

iterable = 0
while iterable < 10:
    try:
        for a,b,c in billboard:
            billboard_a.append(a)
            billboard_b.append(b)
            billboard_c.append(c)
    except ValueError:
        break

print(billboard_a, billboard_b, billboard_c)     # test print if it works    ## it works as intended!
# Now I only need to zip a and b while ignoring c, because the current spot or meaning of c is irrelevant for where we are going we dont need it


#name_var, result_var, rank_var = map(billboard)    # this waits until further work # might be time now    ## this line is a complete waste at this point




        # result_var = int(result_var)    #would maybe work without this line and declaring integer in the next line???
        #billboard.append(name_var +  result_var + rank_var)    # I don't know what I was thinking here


print("test print: ", billboard)    # test print: lets see where we are    # yay something works!

existing_billboard.close()


#billboard_to_swap = billboard.copy()
billboard_to_sort = billboard.copy()


#sorted_billboard = dict(sorted(billboard_to_sort.items(), key=lambda item: item[1]))    #this will have to wait a bit
#print("test print where we are?", sorted_billboard)    # test print where we are


