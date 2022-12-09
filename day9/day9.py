f = open("input.txt")

# Part 1

head = (0, 0)
tail = (0, 0)

def overlapping(tail, head):
    x1, y1 = tail
    x2, y2 = head
    if tail == head:
        return True
    elif x1 == x2:
        if abs(y1 - y2) == 1:
            return True
        else:
            return False
    elif y1 == y2:
        if abs(x1 - x2) == 1:
            return True
        else:
            return False
    else:
        if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
            return True
        else:
            return False

tail_pos = set()
# tail_pos.add(tail)

# for line in f:
#     line = line.strip()
#     dir, mag = line.split()
#     mag = int(mag)
#     if dir == 'R':
#         head = (head[0] + mag, head[1])
#         if overlapping(tail, head):
#             continue
#         else:
#             if head[0] > tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] + 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] > tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] + 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] - 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] - 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             if tail[0] == head[0]:
#                 if head[1] > tail[1]:
#                     for i in range(tail[1], head[1]):
#                         tail_pos.add((tail[0], i))
#                 else:
#                     for i in range(tail[1], head[1], -1):
#                         tail_pos.add((tail[0], i))
#             elif tail[1] == head[1]:
#                 if head[0] > tail[0]:
#                     for i in range(tail[0], head[0]):
#                         tail_pos.add((i, tail[1]))
#                 else :
#                     for i in range(tail[0], head[0], -1):
#                         tail_pos.add((i, tail[1]))
#             tail = (head[0] - 1, head[1])
#     elif dir == 'L':
#         head = (head[0] - mag, head[1])
#         if overlapping(tail, head):
#             continue
#         else:
#             if head[0] > tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] + 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] > tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] + 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] - 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] - 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             if tail[0] == head[0]:
#                 if head[1] > tail[1]:
#                     for i in range(tail[1], head[1]):
#                         tail_pos.add((tail[0], i))
#                 else:
#                     for i in range(tail[1], head[1], -1):
#                         tail_pos.add((tail[0], i))
#             elif tail[1] == head[1]:
#                 if head[0] > tail[0]:
#                     for i in range(tail[0], head[0]):
#                         tail_pos.add((i, tail[1]))
#                 else :
#                     for i in range(tail[0], head[0], -1):
#                         tail_pos.add((i, tail[1]))
#             tail = (head[0] + 1, head[1])
#     elif dir == 'U':
#         head = (head[0], head[1] + mag)
#         if overlapping(tail, head):
#             continue
#         else:
#             if head[0] > tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] + 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] > tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] + 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] - 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] - 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             if tail[0] == head[0]:
#                 if head[1] > tail[1]:
#                     for i in range(tail[1], head[1]):
#                         tail_pos.add((tail[0], i))
#                 else:
#                     for i in range(tail[1], head[1], -1):
#                         tail_pos.add((tail[0], i))
#             elif tail[1] == head[1]:
#                 if head[0] > tail[0]:
#                     for i in range(tail[0], head[0]):
#                         tail_pos.add((i, tail[1]))
#                 else :
#                     for i in range(tail[0], head[0], -1):
#                         tail_pos.add((i, tail[1]))
#             tail = (head[0], head[1] - 1)
#     elif dir == 'D':
#         head = (head[0], head[1] - mag)
#         if overlapping(tail, head):
#             continue
#         else:
#             if head[0] > tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] + 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] > tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] + 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] - 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] - 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             if tail[0] == head[0]:
#                 if head[1] > tail[1]:
#                     for i in range(tail[1], head[1]):
#                         tail_pos.add((tail[0], i))
#                 else:
#                     for i in range(tail[1], head[1], -1):
#                         tail_pos.add((tail[0], i))
#             elif tail[1] == head[1]:
#                 if head[0] > tail[0]:
#                     for i in range(tail[0], head[0]):
#                         tail_pos.add((i, tail[1]))
#                 else :
#                     for i in range(tail[0], head[0], -1):
#                         tail_pos.add((i, tail[1]))
#             tail = (head[0], head[1] + 1)
#     tail_pos.add(tail)

# print(len(tail_pos))

# Part 2

# tail_pos only needs to track last tail position

head_start = (0, 0)

tail_list = [(0, 0)]*9

f_sim = open('sim.txt')

# def move_tail(tail: tuple, head: tuple, dir, mag, tail_pos: set):
#     if dir == 'R':
#         head = (head[0] + mag, head[1])
#         if overlapping(tail, head):
#             tail_pos.add(tail)
#             return tail
#         else:
#             if head[0] > tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] + 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] > tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] + 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] - 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] - 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             if tail[0] == head[0]:
#                 if head[1] > tail[1]:
#                     for i in range(tail[1], head[1]):
#                         tail_pos.add((tail[0], i))
#                 else:
#                     for i in range(tail[1], head[1], -1):
#                         tail_pos.add((tail[0], i))
#             elif tail[1] == head[1]:
#                 if head[0] > tail[0]:
#                     for i in range(tail[0], head[0]):
#                         tail_pos.add((i, tail[1]))
#                 else :
#                     for i in range(tail[0], head[0], -1):
#                         tail_pos.add((i, tail[1]))
#             tail = (head[0] - 1, head[1])
#     elif dir == 'L':
#         head = (head[0] - mag, head[1])
#         if overlapping(tail, head):
#             tail_pos.add(tail)
#             return tail
#         else:
#             if head[0] > tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] + 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] > tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] + 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] - 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] - 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             if tail[0] == head[0]:
#                 if head[1] > tail[1]:
#                     for i in range(tail[1], head[1]):
#                         tail_pos.add((tail[0], i))
#                 else:
#                     for i in range(tail[1], head[1], -1):
#                         tail_pos.add((tail[0], i))
#             elif tail[1] == head[1]:
#                 if head[0] > tail[0]:
#                     for i in range(tail[0], head[0]):
#                         tail_pos.add((i, tail[1]))
#                 else :
#                     for i in range(tail[0], head[0], -1):
#                         tail_pos.add((i, tail[1]))
#             tail = (head[0] + 1, head[1])
#     elif dir == 'U':
#         head = (head[0], head[1] + mag)
#         if overlapping(tail, head):
#             tail_pos.add(tail)
#             return tail
#         else:
#             if head[0] > tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] + 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] > tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] + 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] - 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] - 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             if tail[0] == head[0]:
#                 if head[1] > tail[1]:
#                     for i in range(tail[1], head[1]):
#                         tail_pos.add((tail[0], i))
#                 else:
#                     for i in range(tail[1], head[1], -1):
#                         tail_pos.add((tail[0], i))
#             elif tail[1] == head[1]:
#                 if head[0] > tail[0]:
#                     for i in range(tail[0], head[0]):
#                         tail_pos.add((i, tail[1]))
#                 else :
#                     for i in range(tail[0], head[0], -1):
#                         tail_pos.add((i, tail[1]))
#             tail = (head[0], head[1] - 1)
#     elif dir == 'D':
#         head = (head[0], head[1] - mag)
#         if overlapping(tail, head):
#             tail_pos.add(tail)
#             return tail
#         else:
#             if head[0] > tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] + 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] > tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] + 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] > tail[1]:
#                 tail = (tail[0] - 1, tail[1] + 1)
#                 tail_pos.add(tail)
#             elif head[0] < tail[0] and head[1] < tail[1]:
#                 tail = (tail[0] - 1, tail[1] - 1)
#                 tail_pos.add(tail)
#             if tail[0] == head[0]:
#                 if head[1] > tail[1]:
#                     for i in range(tail[1], head[1]):
#                         tail_pos.add((tail[0], i))
#                 else:
#                     for i in range(tail[1], head[1], -1):
#                         tail_pos.add((tail[0], i))
#             elif tail[1] == head[1]:
#                 if head[0] > tail[0]:
#                     for i in range(tail[0], head[0]):
#                         tail_pos.add((i, tail[1]))
#                 else :
#                     for i in range(tail[0], head[0], -1):
#                         tail_pos.add((i, tail[1]))
#             tail = (head[0], head[1] + 1)
#     tail_pos.add(tail)
#     return tail

def move_tail(tail, head, positions):
    while not overlapping(tail, head):
        if head[0] > tail[0] and head[1] > tail[1]:
            tail = (tail[0] + 1, tail[1] + 1)
        elif head[0] > tail[0] and head[1] < tail[1]:
            tail = (tail[0] + 1, tail[1] - 1)
        elif head[0] < tail[0] and head[1] > tail[1]:
            tail = (tail[0] - 1, tail[1] + 1)
        elif head[0] < tail[0] and head[1] < tail[1]:
            tail = (tail[0] - 1, tail[1] - 1)
        elif tail[0] == head[0]:
            if head[1] > tail[1]:
                tail = (tail[0], tail[1] + 1)
            else:
                tail = (tail[0], tail[1] - 1)
        elif tail[1] == head[1]:
            if head[0] > tail[0]:
                tail = (tail[0] + 1, tail[1])
            else:
                tail = (tail[0] - 1, tail[1])
        positions.add(tail)
    return tail


junk_set = set()
tail_pos = set()
f_e = open('sim_easy.txt')

for line in f_sim:
    line = line.strip()
    line = line.split()
    dir, mag = line[0], int(line[1])
    if dir == 'R':
        head_start = (head[0] + mag, head[1])
    if dir == 'L':
        head_start = (head[0] - mag, head[1])
    if dir == 'U':
        head_start = (head[0], head[1] + mag)
    if dir == 'D':
        head_start = (head[0], head[1] - mag)
    for i, tail in enumerate(tail_list):
        if i == 0:
            tail_list[i] = move_tail(tail, head_start, junk_set)
        elif i == 8:
            tail_pos.add(tail)
            tail_list[i] = move_tail(tail, tail_list[i-1], tail_pos)
        else:
            tail_list[i] = move_tail(tail, tail_list[i-1],junk_set)

print(tail_pos)
print(len(tail_pos))