f = open("input.txt", "r")
lines = f.readlines()
scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0
lines = [line.replace("\n","") for line in lines]
for line in lines:
    rs_size = len(line)
    comp_size = int(rs_size / 2)
    first_comp = line[:comp_size]
    second_comp = line[comp_size:]
    for letter in set(first_comp):
        if letter in second_comp:
            score += scores.index(letter) + 1
print(score)