def readData():
    n = int(input("Number of nodes: "))
    m = int(input("Number of edges: "))
    weighted = True if input("Weighted (y/n)? ") == "y" else False
    undirected = True if input("Undirected (y/n)? ") == "y" else False

    return n, m, weighted, undirected

def readEdge():
    data = input().split()

    u = int(data[0])
    v = int(data[1])
    w = int(data[2]) if len(data) == 3 else None

    return u, v, w

def createAdjacencyMatrix(show=False):
    n, m, weighted, undirected = readData()

    matrix = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = readEdge()

        if weighted:
            matrix[u][v] = w
        else:
            matrix[u][v] = 1
        
        if undirected:
            matrix[v][u] = matrix[u][v]

    if show:
        for i in range(n + 1):
            print(i, ":", matrix[i])

    return matrix

def createAdjacencyList(show=False):
    n, m, weighted, undirected = readData()

    adjList = {} 
    for i in range(1, n + 1):
        adjList[i] = []


    for _ in range(m):
        u, v, w = readEdge()

        if weighted:
            adjList[u].append((u, w))
            if undirected:
                adjList[v].append(v, w)
        else:
            adjList[u].append(v)
            if undirected:
                adjList[v].append(u)

    if show:
        for i in range(1, n + 1):
            print(i, ": ", adjList[i])

    return adjList

def createEdgeList(show=False):
    n, m, weighted, undirected = readData()

    edges = []
    for _ in range(m):
        u, v, w = readEdge()

        if weighted:
            edges.append((u, v, w))
            if undirected:
                edges.append((v, u, w))
        else:
            edges.append((u, v))
            if undirected:
                edges.append((v, u))

    if show:
        print("\n")
        for edge in edges:
            print(edge)

    return edges

if __name__ == "__main__":
    createEdgeList()