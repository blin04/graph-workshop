from reminder1 import createAdjacencyList

def BFS(graph, start=1):

    visited = [False] * (len(graph) + 1)
    queue = [start]

    while queue:
        node = queue.pop(0)

        if visited[node]:
            continue

        visited[node] = True
        print(node, end=' ')
        for neighbour in graph[node]:
            queue.append(neighbour)
        
    print(visited)

def DFS(graph, start=1):

    visited = [False] * (len(graph) + 1)
    stack = [start]

    while stack:
        node = stack.pop()

        if visited[node]:
            continue

        visited[node] = True 
        print(node, end=' ')
        for neighbour in graph[node]:
            stack.append(neighbour)

    print(visited)


if __name__ == "__main__":
    graph = createAdjacencyList()

    BFS(graph)