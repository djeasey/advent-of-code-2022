f = open("day8/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

num_visible = 0
num_rows = len(lines)
num_cols = len(lines[0])

for row in range(num_rows):
    for col in range(num_cols):
        height = lines[row][col]
        visible = False

        # Outer edge visible
        if row == 0 or col == 0 or row == num_rows - 1 or col == num_cols - 1:
            visible = True

        # Look left
        for i in range(0, col):
            compare = lines[row][i]
            if compare >= height:
                break
            if i == col - 1:
                visible = True

        # Look right
        for i in range(col + 1, num_cols):
            compare = lines[row][i]
            if compare >= height:
                break
            if i == num_cols - 1:
                visible = True

        # Look up
        for i in range(0, row):
            compare = lines[i][col]
            if compare >= height:
                break
            if i == row - 1:
                visible = True

        # Look down
        for i in range(row + 1, num_rows):
            compare = lines[i][col]
            if compare >= height:
                break
            if i == num_rows - 1:
                visible = True

        if visible == True:
            num_visible += 1

print(num_visible)
