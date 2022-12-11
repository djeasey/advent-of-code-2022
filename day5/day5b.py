f = open("day5/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
stacks = []

for i in range(9):  # stacks
    stacks.append([])
    for j in range(8):  # lines
        new_element = lines[7 - j][i * 4 + 1]
        if new_element != " ":
            stacks[i].append(new_element)

for line in lines[10:]:
    split_line = line.split(" ")
    num_to_move = int(split_line[1])
    from_pos = int(split_line[3]) - 1
    to_pos = int(split_line[5]) - 1
    temp_array = []
    for i in range(num_to_move):
        moved_element = stacks[from_pos].pop()
        temp_array.append(moved_element)
    for i in range(num_to_move):
        moved_element = temp_array.pop()
        stacks[to_pos].append(moved_element)

output = ""

for stack in stacks:
    output += stack.pop()

print(output)
