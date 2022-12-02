f = open("input.txt", "r")
lines = f.readlines()
calories = 0
calories_list = []
winning_calories = 0
for line in lines:
    if line != "\n":
        calories = calories + int(line.replace("\n",""))
    else:
        calories_list.append(calories)
        calories = 0
calories_list.sort()
calories_list.reverse()
print(calories_list[0]+calories_list[1]+calories_list[2])