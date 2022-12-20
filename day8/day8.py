filename = 'input.txt'
# filename = 'sim.txt'

def main():
    print("Solution to Part 1: ", part1(filename))
    print("Solution to Part 2: ", part2(filename))

def generate_grid(lines):
    grid = [[int(char) for char in line.strip()] for line in lines]
    return grid

def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    grid = generate_grid(lines)
    
    rowsize = len(grid)
    colsize = len(grid[0])
    visible = colsize * 2 + (rowsize - 2) * 2
    for i in range(1, rowsize - 1):
        for j in range(1, colsize - 1):
            if all([grid[r][j] < grid[i][j] for r in range(0, i)]) or all([grid[i][j] > grid[r][j] for r in range(i+1, rowsize)]) or all([grid[i][c]  < grid[i][j] for c in range(0, j)]) or all([grid[i][j] > grid[i][c] for c in range(j+1, colsize)]):
                visible += 1
    return visible

def scenic_score(grid, i, j):
    rowsize = len(grid)
    colsize = len(grid[0])
    l = 0
    r = 0
    u = 0
    d = 0
    for row in range(i - 1, -1, -1):
        if grid[row][j] < grid[i][j]:
            u += 1
        else:
            u += 1
            break
    for row in range(i + 1, rowsize):
        if grid[row][j] < grid[i][j]:
            d += 1
        else:
            d += 1
            break
    for col in range(j - 1, -1, -1):
        if grid[i][col] < grid[i][j]:
            l += 1
        else:
            l += 1
            break   
    for col in range(j+1, colsize):
        if grid[i][col] < grid[i][j]:
            r += 1
        else:
            r += 1
            break
    return l * r * u * d

def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    grid = generate_grid(lines)
    
    rowsize = len(grid)
    colsize = len(grid[0])
    scenic_scores = []
    for i in range(1, rowsize - 1):
        for j in range(1, colsize - 1):
            scenic_scores.append(scenic_score(grid, i, j))
    max_scenic_score = max(scenic_scores)
    return max_scenic_score

main()