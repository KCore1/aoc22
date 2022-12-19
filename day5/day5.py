"""     [G]         [D]     [Q]    
[P]     [T]         [L] [M] [Z]    
[Z] [Z] [C]         [Z] [G] [W]    
[M] [B] [F]         [P] [C] [H] [N]
[T] [S] [R]     [H] [W] [R] [L] [W]
[R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
[C] [N] [H] [R] [N] [H] [D] [J] [Q]
[N] [D] [M] [G] [Z] [F] [W] [S] [S]
 1   2   3   4   5   6   7   8   9 """

from collections import deque

s1 = deque(['N', 'C', 'R', 'T', 'M', 'Z', 'P'])
s2 = deque(['D', 'N', 'T', 'S', 'B', 'Z'])
s3 = deque(['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'])
s4 = deque(['G', 'R', 'Z'])
s5 = deque(['Z', 'N', 'R', 'H'])
s6 = deque(['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'])
s7 = deque(['W', 'D', 'Z', 'R', 'C', 'G', 'M'])
s8 = deque(['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'])
s9 = deque(['S', 'Q', 'P', 'W', 'N'])

stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

f = open('input.txt')

for line in f:
    line = line.strip()
    line = line.split()
    to_move, stack1, stack2 = [int(x) for x in line if x.isdigit()]
    
    # for part 2
    in_transit = []
    for _ in range(to_move):
        n = stacks[stack1 - 1].pop()
        in_transit.append(n)
    
    in_transit = in_transit[::-1]
    for n in in_transit:
        stacks[stack2 - 1].append(n)

for stack in stacks:
    print(stack.pop(), end='')