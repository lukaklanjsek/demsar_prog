import sys

file_name_var = ""    # lets see if we need this
name_var = ""
result_var = 0
rank_var = 0    # high suspicion this does not need to be in the process

#lets make a dictionary with key:value of name_var and result_var
billboard = dict(name_var:result_var)

new_line = map(billboard, sys.argv[1:3])

existing_billboard = open("example.txt", "r")
[for a, b, c in existing_billboard:]
