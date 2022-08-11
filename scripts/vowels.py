# Write the solution for "Filter Vowels".

import re 

file = open("./inputs/vowels.txt", "r")
text = file.read()

my_dict = {x: len(re.findall(f"{x}", text)) for x in "aeiou"}

total = 0

for number, val in my_dict.items():
    total += val

with open("vowels-" + str(total) + ".txt", "w") as f:
    f.write(text)


