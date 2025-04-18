import sys
import json

new_line = " ".join(sys.argv[1:]).split()
#new_line = input("enter name, score and category:")     # TEST INPUT VALUE BY CONSOLE    <- do we need this?

with open("example.json", "r") as test_file:
    existing_billboard = json.load(test_file)

name, score, category = map(str, new_line.split())
length_billboard = len(existing_billboard)

entry11 = {f"entry{length_billboard+1}": {"name": name, "score": score, "category": category}}
existing_billboard.update(entry11)
sorted_billboard = list(sorted(existing_billboard.items(), key=lambda item: item[1]["score"]))

sorted_billboard = dict(sorted_billboard[:10])

with open("example.json", "w") as outfile:
    json.dump(sorted_billboard, outfile, indent=2)
    print(f"Successfully added {new_line} to the score board.")
