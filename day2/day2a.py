f = open("input.txt", "r")
lines = f.readlines()
score = 0
for line in lines:
    plays = line.split(" ")
    them = line[0]
    you = line[2]
    if you == "X":  # Rock
        score += 1
        if them == "A":  # Rock
            score += 3
        if them == "B":  # Paper
            score += 0
        if them == "C":  # Scissors
            score += 6
    if you == "Y":  # Paper
        score += 2
        if them == "A":  # Rock
            score += 6
        if them == "B":  # Paper
            score += 3
        if them == "C":  # Scissors
            score += 0
    if you == "Z":  # Scissors
        score += 3
        if them == "A":  # Rock
            score += 0
        if them == "B":  # Paper
            score += 6
        if them == "C":  # Scissors
            score += 3
print(score)
