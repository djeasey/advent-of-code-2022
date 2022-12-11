f = open("day4/input.txt", "r")
lines = f.readlines()
count = 0
for line in lines:
    assigns = line.strip().split(",")
    first_start = int(assigns[0].split("-")[0])
    first_end = int(assigns[0].split("-")[1])
    second_start = int(assigns[1].split("-")[0])
    second_end = int(assigns[1].split("-")[1])
    if (first_start <= second_start and second_end <= first_end) or (
        second_start <= first_start and first_end <= second_end
    ):
        count += 1
print(count)
