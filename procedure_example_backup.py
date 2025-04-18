#import sys
import json

#new_line = " ".join(sys.argv[1:]).split()
new_line = input("enter name, score and category:")

#existing_billboard = open("example.txt", "r")
#existing_billboard = open("example.json", "r")
with open("example.json", "r") as test_file:
    existing_billboard = json.load(test_file)

#print(existing_billboard)    # TEST PRINT     <-  yeet this before using

name, score, category = map(str, new_line.split())
length_billboard = len(existing_billboard)

entry11 = {f"entry{length_billboard+1}": {"name": name, "score": score, "category": category}}
#print(type(entry11), entry11)    # TEST PRINT    <- yeet
#print(len(existing_billboard), "TEST PRINT")     # TEST PRINT     <- yeet
existing_billboard.update(entry11)
#print(existing_billboard)     # TEST PRINT     <-  yeet
sorted_billboard = dict(
    sorted(existing_billboard.items(), key=lambda item: item[1]["score"]))

print(sorted_billboard)    # TEST PRINT    <-    yeet


with open("example.json", "w") as outfile:
    json.dump(sorted_billboard[:10], outfile, indent=2)



#billboard = []

#ind = 0
#while ind < 10:
#    billboard.append(tuple(existing_billboard.readline().split()))
#    ind += 1

#existing_billboard.close()

#billboard.append(new_line)

#sorted_billboard = sorted(billboard, key=lambda a: a[1])

#billboard_list = [list(t) for t in sorted_billboard]

#combined_billboard = [' '.join(sublist) + "\n" for sublist in billboard_list]

#combined_billboard = combined_billboard[:10]

#new_billboard = open("example.txt", "w")

#new_billboard.writelines(combined_billboard)

#new_billboard.close()