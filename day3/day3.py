import string

alphabet_l = list(string.ascii_lowercase)
alphabet_u = list(string.ascii_uppercase)

alphabet = alphabet_l + alphabet_u

priorities = {k: v + 1 for v, k in enumerate(alphabet)}

score = 0

# Part 1

for line in open("input.txt"):
    line = line.strip()
    sack1 = line[:len(line) // 2]
    sack2 = line[len(line) // 2:]
    sack1 = set(sack1)
    sack2 = set(sack2)
    same = sack1.intersection(sack2)
    score += priorities[same.pop()]

# print(score)

# Part 2

score = 0

f = open("input.txt")
lines = f.readlines()
lines = [l.strip() for l in lines]

splitter = len(lines)
splitter = [s for s in range(splitter) if (s) % 3 == 0]

print(splitter, len(lines))

for s in splitter:
    group = lines[s:s+3]
    sets = []
    for elf in group:
        sets.append(set(elf))
    badge = set.intersection(*sets)
    print(badge)
    score += priorities[badge.pop()]

print(score)