# Write the solution for "Longest Word".
import re

file = open('./inputs/longest.txt', "r")
big_string = file.read()

word_pattern = "\w+"

regex = re.compile(word_pattern)
found = regex.findall(big_string)

if found:
    longest_word = max(found, key=lambda word: len(word))
    result = big_string.replace(longest_word, "**" + longest_word + "**")

    with open('longest_solution.txt', 'w') as f:
        f.write(result)

