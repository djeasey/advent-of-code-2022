f = open("day12/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
letter_order = "SabcdefghijklmnopqrstuvwxyzE"
letter_order = letter_order[::-1]

shortest_distance_array = []
end_positions = []
for i in range(len(lines)):
    shortest_distance_array.append([])
    for j in range(len(lines[0])):
        if lines[i][j] == "E":
            shortest_distance_array[i].append(0)
        else:
            shortest_distance_array[i].append(-1)
        if lines[i][j] == "a":
            end_positions.append([i, j])

current_distance = 0
while len([a for a in end_positions if shortest_distance_array[a[0]][a[1]] != -1]) == 0:
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if shortest_distance_array[i][j] == current_distance:
                last_letter_order = letter_order.find(lines[i][j])
                if i > 0:
                    if (
                        letter_order.find(lines[i - 1][j]) <= last_letter_order + 1
                        and shortest_distance_array[i - 1][j] == -1
                    ):
                        shortest_distance_array[i - 1][j] = current_distance + 1
                if i < len(lines) - 1:
                    if (
                        letter_order.find(lines[i + 1][j]) <= last_letter_order + 1
                        and shortest_distance_array[i + 1][j] == -1
                    ):
                        shortest_distance_array[i + 1][j] = current_distance + 1
                if j > 0:
                    if (
                        letter_order.find(lines[i][j - 1]) <= last_letter_order + 1
                        and shortest_distance_array[i][j - 1] == -1
                    ):
                        shortest_distance_array[i][j - 1] = current_distance + 1
                if j < len(lines[0]) - 1:
                    if (
                        letter_order.find(lines[i][j + 1]) <= last_letter_order + 1
                        and shortest_distance_array[i][j + 1] == -1
                    ):
                        shortest_distance_array[i][j + 1] = current_distance + 1
    current_distance += 1

print(current_distance)
