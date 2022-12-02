f = open("input.txt", "r")
lines = f.readlines()
calories = 0
winning_calories = 0
for line in lines:
    if line != "\n":
        calories = calories + int(line.replace("\n",""))
    else:
        if calories > winning_calories:
            winning_calories = calories
        calories = 0
print(winning_calories)