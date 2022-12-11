f = open("input.txt", "r")
lines = f.readlines()
scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0
lines = [line.replace("\n", "") for line in lines]
for i in range(int(len(lines) / 3)):
    line1 = lines[i * 3 + 0]
    line2 = lines[i * 3 + 1]
    line3 = lines[i * 3 + 2]
    for letter in set(line1):
        if letter in line2:
            if letter in line3:
                score += scores.index(letter) + 1
print(score)
