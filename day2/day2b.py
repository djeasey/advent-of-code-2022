f = open("input.txt", "r")
lines = f.readlines()
score = 0
for line in lines:
    plays = line.split(" ")
    them = line[0]
    you = line[2]
    if you == "X":  # Lose
        score += 0
        if them == "A":  # Rock
            score += 3  # Scissors
        if them == "B":  # Paper
            score += 1  # Rock
        if them == "C":  # Scissors
            score += 2  # Paper
    if you == "Y":  # Draw
        score += 3
        if them == "A":  # Rock
            score += 1  # Rock
        if them == "B":  # Paper
            score += 2  # Paper
        if them == "C":  # Scissors
            score += 3  # Scissors
    if you == "Z":  # Win
        score += 6
        if them == "A":  # Rock
            score += 2  # Paper
        if them == "B":  # Paper
            score += 3  # Scissors
        if them == "C":  # Scissors
            score += 1  # Rock
print(score)
