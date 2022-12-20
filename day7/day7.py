from collections import deque
filename = 'input.txt'
# filename = 'sim.txt'

def main():
    print("Solution to Part 1: ", part1(filename))
    print("Solution to Part 2: ", part2(filename))

def calc_dir_size(filetree, dir):
    size = 0
    for item in filetree[dir]:
        if type(item) == int:
            size += item
        else:
            size += calc_dir_size(filetree, item)
    return size

def part1(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    sizes = {}
    filetree = {}
    dirstack = deque()
    current_dir = ''
    for line in lines:
        line = line.strip().split()
        if line[0] == '$' and line[1] == 'cd':
            if line[2] == '..':
                current_dir = dirstack.pop()
            else:
                dirstack.append(current_dir)
                if line[2] == '/':
                    current_dir = '/'
                elif current_dir == '/':
                    current_dir = current_dir + line[2]
                else:
                    current_dir = current_dir + '/' + line[2]
        elif line[0] == '$' and line[1] == 'ls':
            filetree[current_dir] = []
            continue
        elif line[0] == 'dir':
            if current_dir == '/':
                filetree[current_dir].append(current_dir + line[1])
            else:
                filetree[current_dir].append(current_dir + '/' + line[1])
        else:
            filetree[current_dir].append(int(line[0]))
    
    for dir in filetree:
        sizes[dir] = calc_dir_size(filetree, dir)
    
    total = sum(size if size <= 100000 else 0 for size in sizes.values())
    
    return total

def part2(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    sizes = {}
    filetree = {}
    dirstack = deque()
    current_dir = ''
    for line in lines:
        line = line.strip().split()
        if line[0] == '$' and line[1] == 'cd':
            if line[2] == '..':
                current_dir = dirstack.pop()
            else:
                dirstack.append(current_dir)
                if line[2] == '/':
                    current_dir = '/'
                elif current_dir == '/':
                    current_dir = current_dir + line[2]
                else:
                    current_dir = current_dir + '/' + line[2]
        elif line[0] == '$' and line[1] == 'ls':
            filetree[current_dir] = []
            continue
        elif line[0] == 'dir':
            if current_dir == '/':
                filetree[current_dir].append(current_dir + line[1])
            else:
                filetree[current_dir].append(current_dir + '/' + line[1])
        else:
            filetree[current_dir].append(int(line[0]))
    
    for dir in filetree:
        sizes[dir] = calc_dir_size(filetree, dir)

    need_to_free = 30000000 - (70000000 - sizes['/'])

    possible_dirs = {dir: size for dir, size in sizes.items() if size >= need_to_free}

    return min(possible_dirs.values())

main()