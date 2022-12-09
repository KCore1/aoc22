win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}
draw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}
shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

score = 0

# Part 1

for line in open("input.txt"):
    strat = line.split()
    if win[strat[0]] == strat[1]:
        score += 6 + shape_score[strat[1]]
    elif draw[strat[0]] == strat[1]:
        score += 3 + shape_score[strat[1]]
    else:
        score += shape_score[strat[1]]

print(score)

# Part 2

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

score = 0

for line in open("input.txt"):
    strat = line.split()
    if strat[1] == "X":
        score += shape_score[lose[strat[0]]]
    if strat[1] == "Y":
        score += 3 + shape_score[draw[strat[0]]]
    if strat[1] == "Z":
        score += 6 + shape_score[win[strat[0]]]

print(score)