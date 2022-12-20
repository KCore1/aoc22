filename = 'input.txt'
# filename = 'sim.txt'

def main():
    print("Solution to Part 1: ", part1(filename))
    print("Solution to Part 2: ", part2(filename))

def part1(filename):
    with open(filename) as f:
        line = f.readline()
        found_marker = False
        index = 0
        while not found_marker:
            to_check = set(line[index:index + 4])
            if len(to_check) == 4:
                found_marker = True
            else:
                index += 4
    return index + 3

def part2(filename):
    with open(filename) as f:
        line = f.readline()
        found_marker = False
        index = 0
        while not found_marker:
            to_check = set(line[index:index + 14])
            if len(to_check) == 14:
                found_marker = True
            else:
                index += 1
    return index + 14

main()