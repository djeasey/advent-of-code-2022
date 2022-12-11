f = open("day10/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

X = 1

line_pos = 0
change_in_prog = False

draw_list = []

for cycle in range(0, 240):
    if cycle > 0 and cycle % 40 == 0:
        X = X + 40
    if cycle == X - 1 or cycle == X or cycle == X + 1:
        draw_list.append("#")
    else:
        draw_list.append(".")

    if lines[line_pos] == "noop":
        line_pos += 1
    else:
        if not change_in_prog:
            change_in_prog = True
        else:
            X += int(lines[line_pos].split(" ")[1])
            line_pos += 1
            change_in_prog = False

print("".join(draw_list[0:40]))
print("".join(draw_list[40:80]))
print("".join(draw_list[80:120]))
print("".join(draw_list[120:160]))
print("".join(draw_list[160:200]))
print("".join(draw_list[200:240]))
