f = open("day9/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

head_pos = [0, 0]
tail_pos = [0, 0]

tail_positions = []

for line in lines:
    split_line = line.split(" ")
    for i in range(int(split_line[1])):
        if split_line[0] == "R":
            head_pos[0] += 1
        if split_line[0] == "L":
            head_pos[0] -= 1
        if split_line[0] == "U":
            head_pos[1] += 1
        if split_line[0] == "D":
            head_pos[1] -= 1
        if abs(head_pos[0] - tail_pos[0]) > 1 and abs(head_pos[1] - tail_pos[1]) == 0:
            if head_pos[0] > tail_pos[0]:
                tail_pos[0] += 1
            else:
                tail_pos[0] -= 1
        elif abs(head_pos[0] - tail_pos[0]) == 0 and abs(head_pos[1] - tail_pos[1]) > 1:
            if head_pos[1] > tail_pos[1]:
                tail_pos[1] += 1
            else:
                tail_pos[1] -= 1
        elif abs(head_pos[0] - tail_pos[0]) > 0 and abs(head_pos[1] - tail_pos[1]) > 0:
            if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
                if head_pos[0] > tail_pos[0]:
                    tail_pos[0] += 1
                else:
                    tail_pos[0] -= 1
                if head_pos[1] > tail_pos[1]:
                    tail_pos[1] += 1
                else:
                    tail_pos[1] -= 1

        if tail_pos not in tail_positions:
            tail_positions.append(tail_pos.copy())

print(len(tail_positions))
