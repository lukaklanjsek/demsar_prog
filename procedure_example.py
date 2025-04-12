import sys

new_line = " ".join(sys.argv[1:]).split()

existing_billboard = open("example.txt", "r")
billboard = []

ind = 0
while ind < 10:
    billboard.append(tuple(existing_billboard.readline().split()))
    ind += 1

existing_billboard.close()

billboard.append(new_line)

sorted_billboard = sorted(billboard, key=lambda a: a[1])

billboard_list = [list(t) for t in sorted_billboard]

combined_billboard = [' '.join(sublist) + "\n" for sublist in billboard_list]

combined_billboard = combined_billboard[:10]

new_billboard = open("example.txt", "w")

new_billboard.writelines(combined_billboard)

new_billboard.close()