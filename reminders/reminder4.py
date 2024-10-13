import math
from reminder1 import createAdjacencyList

INF = 1e9

def heuristic(node1, node2):
    lat1 = math.radians(node1[0])
    lon1 = math.radians(node1[1])
    lat2 = math.radians(node2[0])
    lon2 = math.radians(node2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of Earth in kilometers (use 3956 for miles)
    R = 6371.0
    
    # Calculate the distance
    distance = R * c
    
    return distance

def astar(graph, start, end, coordinates):
    distances = [INF] * (len(graph) + 1)
    visited = [False] * (len(graph) + 1)
    parents = [None] * (len(graph) + 1)

    distances[start] = 0
    queue = [(start, 0)]
    while queue:
        queue.sort(key=lambda x: x[1])

        node, _ = queue.pop(0)
        currDistance = distances[node]

        if node == end:
            break

        if visited[node]: continue
        else: visited[node] = True

        for neighbour, length  in graph[node]:
            if currDistance + length < distances[neighbour]:
                distances[neighbour] = currDistance + length
                parents[neighbour] = node
                queue.append((neighbour, distances[neighbour] + heuristic(coordinates[neighbour], coordinates[end])))

    return distances, parents

def getPath(node, graph, parents):
    path = []
    while parents[node] is not None:
        path.append(node) 
        node = parents[node]
    path.append(node)
    path.reverse()
    return path


if __name__ == "__main__":
    graph = createAdjacencyList()

    cityIndexes = {}
    nodeLabels = {}
    nodeCoordinates = {}
    with open("../graph/nodesCoordinates") as f:
        for line in f:
            line = line.strip('\n')
            line = line.split(' ')
            cityIndexes[line[1]] = int(line[0])
            nodeLabels[int(line[0])] = line[1]
            nodeCoordinates[int(line[0])] = (float(line[2]), float(line[3]))

    start = input("Pocetni grad: ")
    end = input("Destinacija: ")

    startNode = cityIndexes[start]
    endNode = cityIndexes[end]

    distances, parents = astar(graph, startNode, endNode, nodeCoordinates)
    
    path = getPath(endNode, graph, parents)

    toPrint = ""
    for node in path:
        toPrint += nodeLabels[node]

        if node != path[-1]:
            toPrint += " -> "
    print(toPrint + " (" + str(distances[endNode]) + "km)")