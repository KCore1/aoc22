# filename = 'sim.txt'
filename = 'input.txt'

def main():
    print('Solution to Part 1: ', part1(filename))
    print('Solution to Part 2:')
    print(part2(filename))

def part1(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    x = 1
    cycle = 1
    to_add = []
    counter = 1
    for line in lines:       
        line = line.strip().split() 
        instruction = line[0]
        if instruction == 'addx':
            cycle += 1
            if cycle % 40 == 20:
                to_add.append(cycle * x)
            cycle += 1
            x += int(line[1])
            if cycle % 40 == 20:
                to_add.append(cycle * x)
        elif instruction == 'noop':
            cycle += 1
            if cycle % 40 == 20:
                to_add.append(cycle * x)
        counter += 1

    return sum(to_add)

def draw_pixel(x, cycle, row):
    if (cycle - 1) % 40 in range(x - 1, x + 2):
        row += '#'
    else:
        row += '.'
    return row

def part2(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    x = 1
    cycle = 0
    counter = 1
    row = ''
    rows = []
    for line in lines:       
        line = line.strip().split() 
        instruction = line[0]
        if instruction == 'addx':
            cycle += 1
            row = draw_pixel(x, cycle, row)
            if cycle % 40 == 0:
                rows.append(row)
                row = ''
            cycle += 1
            row = draw_pixel(x, cycle, row)
            x += int(line[1])
            if cycle % 40 == 0:
                rows.append(row)
                row = ''
        elif instruction == 'noop':
            cycle += 1
            row = draw_pixel(x, cycle, row)
            if cycle % 40 == 0:
                rows.append(row)
                row = ''
        counter += 1

    return '\n'.join(rows)

main()