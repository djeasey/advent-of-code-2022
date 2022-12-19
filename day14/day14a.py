f = open("day14/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
coords = [
    [[int(num) for num in coord.split(",")] for coord in line.split(" -> ")]
    for line in lines
]

height = max([max([coord[1] for coord in line]) for line in coords]) + 1

grid = [["." for i in range(1000)] for j in range(height + 2)]

for line in coords:
    for index in range(len(line) - 1):
        current_j = line[index][0]
        current_i = line[index][1]
        next_j = line[index + 1][0]
        next_i = line[index + 1][1]
        if current_j == next_j:
            if current_i < next_i:
                for i in range(current_i, next_i + 1):
                    grid[i][current_j] = "#"
            else:
                for i in range(next_i, current_i + 1):
                    grid[i][current_j] = "#"
        else:
            if current_j < next_j:
                for j in range(current_j, next_j + 1):
                    grid[current_i][j] = "#"
            else:
                for j in range(next_j, current_j + 1):
                    grid[current_i][j] = "#"

count = 0
while True:
    i = 0
    j = 500
    finished = False
    while not finished:
        if i == height:
            print(count)
            quit()
        if grid[i + 1][j] == ".":
            i += 1
        elif grid[i + 1][j - 1] == ".":
            i += 1
            j -= 1
        elif grid[i + 1][j + 1] == ".":
            i += 1
            j += 1
        else:
            grid[i][j] = "o"
            finished = True
            count += 1
