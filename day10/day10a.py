f = open("day10/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

cycle = 1
X = 1
total = 0

for line in lines:
    if cycle in (20, 60, 100, 140, 180, 220):
        total += cycle * X
    if line == "noop":
        cycle += 1
    else:
        if cycle + 1 in (20, 60, 100, 140, 180, 220):
            total += (cycle + 1) * X
        X += int(line.split(" ")[1])
        cycle += 2

print(total)
