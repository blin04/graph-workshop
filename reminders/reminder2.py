from reminder1 import createAdjacencyList

def BFS(adjList, start=1):

    visited = [False] * (len(adjList) + 1)
    queue = [start]

    while queue:
        node = queue.pop(0)

        if visited[node]:
            continue

        visited[node] = True
        print(node, end=' ')
        for neighbour in adjList[node]:
            queue.append(neighbour)
        
    print(visited)

def DFS(adjList, start=1):

    visited = [False] * (len(adjList) + 1)
    stack = [start]

    while stack:
        node = stack.pop()

        if visited[node]:
            continue

        visited[node] = True 
        print(node, end=' ')
        for neighbour in adjList[node]:
            stack.append(neighbour)

    print(visited)


if __name__ == "__main__":
    adjList = createAdjacencyList()

    BFS(adjList)