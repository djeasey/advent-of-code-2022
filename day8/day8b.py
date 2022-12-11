f = open("day8/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

num_visible = 0
num_rows = len(lines)
num_cols = len(lines[0])

max_scenic_score = 0

for row in range(num_rows):
    for col in range(num_cols):
        height = lines[row][col]

        # Look left
        left_view = 0
        for i in range(col - 1, -1, -1):
            left_view += 1
            compare = lines[row][i]
            if compare >= height:
                break

        # Look right
        right_view = 0
        for i in range(col + 1, num_cols):
            right_view += 1
            compare = lines[row][i]
            if compare >= height:
                break

        # Look up
        up_view = 0
        for i in range(row - 1, -1, -1):
            up_view += 1
            compare = lines[i][col]
            if compare >= height:
                break

        # Look down
        down_view = 0
        for i in range(row + 1, num_rows):
            down_view += 1
            compare = lines[i][col]
            if compare >= height:
                break

        scenic_score = left_view * right_view * up_view * down_view

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)
