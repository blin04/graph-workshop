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

    distances, parents = dijkstra(graph, 1)
    
    print(getPath(3, graph, parents))

