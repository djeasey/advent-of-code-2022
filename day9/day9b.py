f = open("day9/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

rope = [[0, 0] for i in range(10)]

tail_positions = []

for line in lines:
    split_line = line.split(" ")
    for i in range(int(split_line[1])):
        if split_line[0] == "R":
            rope[0][0] += 1
        if split_line[0] == "L":
            rope[0][0] -= 1
        if split_line[0] == "U":
            rope[0][1] += 1
        if split_line[0] == "D":
            rope[0][1] -= 1
        for j in range(1, 10):
            if (
                abs(rope[j - 1][0] - rope[j][0]) > 1
                and abs(rope[j - 1][1] - rope[j][1]) == 0
            ):
                if rope[j - 1][0] > rope[j][0]:
                    rope[j][0] += 1
                else:
                    rope[j][0] -= 1
            elif (
                abs(rope[j - 1][0] - rope[j][0]) == 0
                and abs(rope[j - 1][1] - rope[j][1]) > 1
            ):
                if rope[j - 1][1] > rope[j][1]:
                    rope[j][1] += 1
                else:
                    rope[j][1] -= 1
            elif (
                abs(rope[j - 1][0] - rope[j][0]) > 0
                and abs(rope[j - 1][1] - rope[j][1]) > 0
            ):
                if (
                    abs(rope[j - 1][0] - rope[j][0]) > 1
                    or abs(rope[j - 1][1] - rope[j][1]) > 1
                ):
                    if rope[j - 1][0] > rope[j][0]:
                        rope[j][0] += 1
                    else:
                        rope[j][0] -= 1
                    if rope[j - 1][1] > rope[j][1]:
                        rope[j][1] += 1
                    else:
                        rope[j][1] -= 1

        if rope[9] not in tail_positions:
            tail_positions.append(rope[9].copy())

print(len(tail_positions))
