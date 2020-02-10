
file = "input_paper_strip_1"

count = 0
with open(file, "r") as paper:
    for line in paper:
        if line[0] == '|':
            count += line.count('|')

print(count)
