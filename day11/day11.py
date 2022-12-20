from math import floor, pow, gcd
import queue

filename = 'input.txt'
# filename = 'sim.txt'

def main():
    print('Solution to Part 1: ', part1(filename))
    print('Solution to Part 2:', part2(filename))

def monkey_inspection(monkey, operations, tests, results, monkeys):
    items = monkeys[monkey]
    counter = 0
    while not items.empty():
        item = items.get()
        item = floor(operations[monkey](item) / 3)
        if tests[monkey](item):
            monkeys[results[monkey][0]].put(item)
        else:
            monkeys[results[monkey][1]].put(item)
        counter += 1
    return monkeys, counter

def monkey_inspection_2(monkey, operations, tests, results, monkeys, lcm):
    items = monkeys[monkey]
    counter = 0
    while not items.empty():
        item = items.get()
        item = operations[monkey](item) % lcm
        if tests[monkey](item):
            monkeys[results[monkey][0]].put(item)
        else:
            monkeys[results[monkey][1]].put(item)
        counter += 1
    return monkeys, counter

def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    monkeys, operations, tests, results, _ = get_inputs(lines)

    times_inspected = {monkey: 0 for monkey in monkeys}

    for _ in range(20):
        for monkey in monkeys:
            monkeys, count = monkey_inspection(monkey, operations, tests, results, monkeys)
            times_inspected[monkey] += count

    top_monkey = max(times_inspected, key=times_inspected.get)
    second_monkey = max(times_inspected, key=lambda x: times_inspected[x] if x != top_monkey else 0)
        
    return times_inspected[top_monkey] * times_inspected[second_monkey]

def least_common_multiple(nums):
    lcm = nums[0]
    for i in nums[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    monkeys, operations, tests, results, divisors = get_inputs(lines)

    times_inspected = {monkey: 0 for monkey in monkeys}

    lcm = least_common_multiple(divisors)

    for _ in range(10000):
        for monkey in monkeys:
            monkeys, count = monkey_inspection_2(monkey, operations, tests, results, monkeys, lcm)
            times_inspected[monkey] += count

    top_monkey = max(times_inspected, key=times_inspected.get)
    second_monkey = max(times_inspected, key=lambda x: times_inspected[x] if x != top_monkey else 0)
        
    return times_inspected[top_monkey] * times_inspected[second_monkey]

def get_inputs(lines):
    monkeys = {}
    operations = {}
    tests = {}
    results = {}
    divisors = []
    monkey = ''
    for line in lines:
        line = line.strip().split()
        if len(line) == 0:
            continue
        elif line[0] == 'Monkey':
            monkey = line[1][0]
            monkeys[monkey] = queue.Queue()
        elif line[0] == 'Starting':
            for item in line[2:]:
                monkeys[monkey].put(int(item[:2]))
        elif line[0] == 'Operation:':
            if 'old' in line[5]:
                operation = lambda x: pow(x, 2)
            elif '*' in line[4]:
                operand = int(line[5])
                operation = lambda x, operand=operand: x * operand
            elif '+' in line[4]:
                operand = int(line[5])
                operation = lambda x, operand=operand: x + operand
            operations[monkey] = operation
        elif line[0] == 'Test:':
            divisor = int(line[3])
            divisors.append(divisor)
            test = lambda x, divisor=divisor: x % divisor == 0
            tests[monkey] = test
        elif line[0] == 'If' and line[1] == 'true:':
            results[monkey] = [line[5]]
        elif line[0] == 'If' and line[1] == 'false:':
            results[monkey].append(line[5])

    return monkeys, operations, tests, results, divisors

main()