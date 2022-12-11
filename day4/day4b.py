f = open("day4/input.txt", "r")
lines = f.readlines()
count = 0
for line in lines:
    assigns = line.strip().split(",")
    first_set = set(
        range(int(assigns[0].split("-")[0]), int(assigns[0].split("-")[1]) + 1)
    )
    second_set = set(
        range(int(assigns[1].split("-")[0]), int(assigns[1].split("-")[1]) + 1)
    )
    if first_set.intersection(second_set) != set():
        count += 1
print(count)
