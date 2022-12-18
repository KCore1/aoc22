import multiprocessing as mp

# f = open('input.txt')
f = open('sim.txt')

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.keys())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = float('inf')
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph[current_min_node]
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + 1
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

# These functions are from Garrett Moody, who I pair programmed with for some of this challenge

def findPaths(currentPath, newGraph, visited, flowDict, paths, time):

    currentValve = currentPath[-1]
    
    if len(currentPath) == len(newGraph):
        paths.append(currentPath)
        return
   
    biggestScore = max([(time - newGraph[currentValve][x]) * flowDict[x] for x in newGraph[currentValve] if x not in visited])
    if biggestScore < 1:
        paths.append(currentPath)
        return
    for key in newGraph[currentValve]:
        if key not in visited and (time - newGraph[currentValve][key]) * flowDict[key] > biggestScore / 100:
            updatedVisited = set(visited)
            updatedVisited.add(key)
            updatedPath = list(currentPath)
            updatedPath.append(key)  
            tempTime = time - (newGraph[currentValve][key] + 1)
    
            
            findPaths(updatedPath, newGraph, updatedVisited, flowDict, paths, tempTime)

def simulatePath(path, flowDict, newGraph):
    time = 29
    score = 0
    previousValve = 'AA'
    for valve in path:
        if valve == 'AA':
            continue
        flow = flowDict[valve]
        distance = newGraph[previousValve][valve]
        if (time - distance) * flow < 1:
            break
        score += (time - distance) * flow
        time -= distance + 1
        previousValve = valve

    return score

def findPaths2(currentPath, newGraph, visited, flowDict, paths_user, paths_elephant, time):

    currentValve = currentPath[-1]
    
    if len(currentPath) == len(newGraph):
        paths_user.append(currentPath)
        return
   
    biggestScore = max([(time - newGraph[currentValve][x]) * flowDict[x] for x in newGraph[currentValve] if x not in visited])
    if biggestScore < 1:
        paths_user.append(currentPath)
        return
    for key in newGraph[currentValve]:
        if key not in visited:
            updatedVisited = set(visited)
            updatedVisited.add(key)
            updatedPath = list(currentPath)
            updatedPath.append(key)  
            tempTime = time - (newGraph[currentValve][key] + 1)
    
            
            findPaths2(updatedPath, newGraph, updatedVisited, flowDict, paths_user, paths_elephant, tempTime)


adj_matrix = {}
flow_dict = {}
graph = {}

for line in f:
    seg1, seg2 = line.split(';')
    seg1 = seg1.split()
    adj_matrix[seg1[1]] = [valve.strip().replace(',','') for valve in seg2.split()[4:]]
    flow_dict[seg1[1]] = int(seg1[4].split('=')[1])

for valve in adj_matrix.keys():
        graph[valve] = dijkstra_algorithm(adj_matrix, valve)[1]

start_node = 'AA'
current_node = start_node
time = 30
visited_nodes = set()

findPaths2(['AA'], graph, set(['AA']), flowDict, paths, 29)
        
        
print(len(paths))

num_cores = mp.cpu_count()
pool = mp.Pool(num_cores)
maxScores = mp.Manager().list()

for i in range(len(paths) - 1):
    for j in range(i + 1, len(paths)):
        maxScore = max(maxScore, simulatePath2(paths[i], paths[j], flowDict, newGraph))
        # maxScore = max(maxScore, simulatePath2(paths[j], paths[i], flowDict, newGraph))  
    if i % 100 == 0:
        print('ran')

print(maxScore)