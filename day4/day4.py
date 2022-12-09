f = open('input.txt')

# Part 1

# contain_count = 0

# for line in f:
#     line = line.strip()
#     sec1, sec2 = line.split(',')
#     sec1 = sec1.split('-')
#     sec2 = sec2.split('-')
#     sec1 = [int(x) for x in sec1]
#     sec2 = [int(x) for x in sec2]
#     if sec1[0] < sec2[0]:
#         if sec1[1] >= sec2[1]:
#             contain_count += 1
#             print("c")
#     elif sec2[0] < sec1[0]:
#         if sec2[1] >= sec1[1]:
#             contain_count += 1
#             print("c")
#     else:
#         if sec1[1] >= sec2[1]:
#             contain_count += 1
#             print("c")
#         elif sec2[1] >= sec1[1]:
#             contain_count += 1
#             print("c")

# print(contain_count)

# Part 2

overlap_count = 0

for line in f:
    line = line.strip()
    sec1, sec2 = line.split(',')
    sec1 = sec1.split('-')
    sec2 = sec2.split('-')
    sec1 = [int(x) for x in sec1]
    sec2 = [int(x) for x in sec2]
    if sec1[0] < sec2[0]:
        if sec1[1] >= sec2[0]:
            overlap_count += 1
            print("o")
    elif sec2[0] < sec1[0]:
        if sec2[1] >= sec1[0]:
            overlap_count += 1
            print("o")
    else:
        overlap_count += 1
        print("o")

print(overlap_count)