f = open("day11/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
import math

num_of_monkeys = math.ceil(len(lines) / 7)

# Starting setup
monkeys = []
for i in range(num_of_monkeys):
    items = lines[i * 7 + 1].replace(" ", "").split(":")[1].split(",")
    int_items = [int(item) for item in items]
    monkeys.append(int_items)

counts = [0 for i in range(num_of_monkeys)]

lcm = math.prod([int(lines[i * 7 + 3].split(" ")[-1]) for i in range(len(monkeys))])

for round in range(10000):
    for i in range(len(monkeys)):
        operation = lines[i * 7 + 2].split("=")[1]
        test = int(lines[i * 7 + 3].split(" ")[-1])
        if_true = int(lines[i * 7 + 4].split(" ")[-1])
        if_false = int(lines[i * 7 + 5].split(" ")[-1])
        list_to_iterate = monkeys[i]
        monkeys[i] = []
        for old in list_to_iterate:
            counts[i] += 1
            new = eval(operation)
            new = new % lcm
            test_output = new % test == 0
            if test_output:
                monkeys[if_true].append(new)
            else:
                monkeys[if_false].append(new)

counts.sort()

print(counts[-1] * counts[-2])
