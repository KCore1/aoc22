import itertools
import queue
import multiprocessing as mp

filename = 'input.txt'

def main():
    print('Day18 P1', part1())
    print("Day 18 P2: ", part2())

def find_adjacent(block, space):
    num_adj = 0
    for b in space:
        if abs(b[0] - block[0]) + abs(b[1] - block[1]) + abs(b[2] - block[2]) == 1:
            num_adj += 1
    return num_adj

def part1():
    with open(filename) as f:
        space = []
        lines = f.readlines()
        for line in lines:
            block = line.strip()
            block = [int(x) for x in block.split(',')]
            space.append(tuple(block))
    
    sum_sa = 0
    for block in space:
        sum_sa += 6 - find_adjacent(block, space)
    
    return sum_sa

def touches_air(block, space):
    check_range = 20
    visited = set()
    to_visit = queue.Queue()
    to_visit.put(block)
    while not to_visit.empty():
        b = to_visit.get()
        if b in visited:
            continue
        visited.add(b)
        if b in space:
            continue
        if b[0] == check_range or b[1] == check_range or b[2] == check_range:
            print(block, "touches air")
            return True
        for i in range(-1, 2):
            if i == 0:
                continue
            to_visit.put((b[0] + i, b[1], b[2]))
            to_visit.put((b[0], b[1] + i, b[2]))
            to_visit.put((b[0], b[1], b[2] + i))
    print(block, 'does not touch air')
    return False

def find_enclosed(space):
    check_range = 20
    space_all = list(itertools.product(range(check_range + 1), repeat=3))
    airblocks = [block for block in space_all if block not in space]
    print("got airblocks", len(airblocks))
    pool = mp.Pool(mp.cpu_count())
    results = pool.starmap(touches_air, [(b, space) for b in airblocks])
    enclosed_airblocks = [b for b, r in zip(airblocks, results) if not r]
    return enclosed_airblocks


def part2():
    with open(filename) as f:
        space = []
        # checker = [] # find maximum coordinate in x, y, or z
        lines = f.readlines()
        for line in lines:
            block = line.strip()
            block = [int(x) for x in block.split(',')]
            space.append(tuple(block))
            # checker.extend(block)
    # print(max(checker))

    enclosed_airblocks = find_enclosed(space)
    print("num enclosed airblocks", len(enclosed_airblocks))
    sa_airblocks = 0
    sa_total = 0
    for block in enclosed_airblocks:
        sa_airblocks += 6 - find_adjacent(block, enclosed_airblocks)
    for block in space:
        sa_total += 6 - find_adjacent(block, space)
    return sa_total - sa_airblocks

main()