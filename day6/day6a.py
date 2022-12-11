f = open("day6/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

length = 4
for i in range(length - 1, len(lines[0])):
    if len(set([lines[0][i - j] for j in range(length)])) == length:
        print(i + 1)
        break
