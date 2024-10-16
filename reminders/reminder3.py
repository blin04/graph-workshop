from reminder1 import createAdjacencyList

INF = 1e9

def dijkstra(graph, start):
    distances = [INF] * (len(graph) + 1)
    visited = [False] * (len(graph) + 1)
    parents = [None] * (len(graph) + 1)

    distances[start] = 0
    queue = [(start, 0)]
    while queue:
        queue.sort(key=lambda x: x[1])

        node, currDistance = queue.pop(0)

        if node == end:
            break

        if visited[node]: continue
        else: visited[node] = True

        for neighbour, length  in graph[node]:
            if currDistance + length < distances[neighbour]:
                distances[neighbour] = currDistance + length
                parents[neighbour] = node
                queue.append((neighbour, distances[neighbour]))

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
    with open("../graph/nodes") as f:
        for line in f:
            line = line.split(' ')
            cityIndexes[line[1].strip('\n')] = int(line[0])
            nodeLabels[int(line[0])] = line[1].strip('\n')

    start = input("Pocetni grad: ")
    end = input("Destinacija: ")

    startNode = cityIndexes[start]
    endNode = cityIndexes[end]

    distances, parents = dijkstra(graph, startNode)
    
    path = getPath(endNode, graph, parents)

    toPrint = ""
    for node in path:
        toPrint += nodeLabels[node]

        if node != path[-1]:
            toPrint += " -> "
    print(toPrint + " (" + str(distances[endNode]) + "km)")