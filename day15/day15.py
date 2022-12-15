f = open('input.txt')
# f = open('sim.txt')

# every position in row 2000000 where a beacon cannot be

d = dict()
y_t = 2000000
x_lim = 4000000
y_lim = 4000000

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# def add_blocked(x: int, y: int, md: int):
#     # specifically for row 2000000
#     for i in range(x - md, x + md + 1):
#         if manhattan_distance(x, y, i, y_t) <= md:
#             if i not in d.keys():
#                 d[i] = 'X'
#             else:
#                 if d[i] == 'B':
#                     continue
#                 else:
#                     d[i] = 'X'

def tuning_freq(x, y):
    return 4000000 * x + y        

# for line in f:
#     line = line.strip()
#     line = line.split(':')
#     x, y = line[0].split(',')
#     x = x.split(' ')
#     sensorx = int(x[2][2:])
#     sensory = int(y[3:])
#     x, y = line[1].split(',')
#     x = x.split(' ')
#     beaconx = int(x[5][2:])
#     beacony = int(y[3:])
#     if beacony == y_t:
#         d[beaconx] = 'B'

#     md = manhattan_distance(sensorx, sensory, beaconx, beacony)
#     add_blocked(sensorx, sensory, md)

# blocked_in_row_2M = [x for x in d.values() if x == 'X']

# print(len(blocked_in_row_2M))

# Part 2

d = dict()

def find_possible_points(sensors):
    possible = set()
    for sensor in sensors:
        offset = 0
        for i in range(sensor[0][1] - sensor[1] - 1, sensor[0][1]):
            if offset == 0:
                if sensor[0][0] <= 4000000 and sensor[0][0] >= 0 and i <= 4000000 and i >= 0:
                    possible.add((sensor[0][0], i))
            else:
                if sensor[0][0] - offset <= 4000000 and sensor[0][0] - offset >= 0 and i <= 4000000 and i >= 0:
                    possible.add((sensor[0][0] - offset, i))
                if sensor[0][0] + offset <= 4000000 and sensor[0][0] + offset >= 0 and i <= 4000000 and i >= 0:
                    possible.add((sensor[0][0] + offset, i))

            offset += 1

        for i in range(sensor[0][1], sensor[0][1] + sensor[0][1] + 2):
            if offset == 0:
                if sensor[0][0] <= 4000000 and sensor[0][0] >= 0 and i <= 4000000 and i >= 0:
                    possible.add((sensor[0][0], i))
            else:
                if sensor[0][0] - offset <= 4000000 and sensor[0][0] - offset >= 0 and i <= 4000000 and i >= 0:
                    possible.add((sensor[0][0] - offset, i))
                if sensor[0][0] + offset <= 4000000 and sensor[0][0] + offset >= 0 and i <= 4000000 and i >= 0:
                    possible.add((sensor[0][0] + offset, i))

            offset -= 1
    return possible

def find_distress(sensors, possible): # 
    for points, md in sensors:
            to_delete = []
            for coord in possible:
                current = manhattan_distance(points[0], points[1], coord[0], coord[1])
                if current <= md:
                    to_delete.append(coord)
            
            for coord in to_delete:
                possible.remove(coord)

            print("Remaining", len(possible))
    for final in possible:
        final_val = tuning_freq(final[0], final[1])
    return final_val

sensors = []

for line in f:
    line = line.strip()
    line = line.split(':')
    x, y = line[0].split(',')
    x = x.split(' ')
    sensorx = int(x[2][2:])
    sensory = int(y[3:])

    x, y = line[1].split(',')
    x = x.split(' ')
    beaconx = int(x[5][2:])
    beacony = int(y[3:])

    sensors.append(((sensorx, sensory), manhattan_distance(sensorx, sensory, beaconx, beacony)))

print("Gathered sensors")

possible = find_possible_points(sensors)

print("Possible points found: ", len(possible))

print(find_distress(sensors, possible, x_lim, y_lim))