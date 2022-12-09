elves = []
tsum = 0
for line in open("input.txt"):
    if line == "\n":
        elves.append(tsum)
        tsum = 0
    else:
        tsum += int(line)

elves.sort()

print(f"{elves[-1]} + {elves[-2]} + {elves[-3]} = {sum(elves[-3:])}")
