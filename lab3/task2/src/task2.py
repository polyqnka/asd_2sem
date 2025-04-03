import sys

sys.setrecursionlimit(2000)


def dfs(v, graph, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


def count_connected_components(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {i: False for i in range(1, n + 1)}
    components = 0

    for node in range(1, n + 1):
        if not visited[node]:
            components += 1
            dfs(node, graph, visited)

    return components


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n, m = map(int, f.readline().split())
        edges = [tuple(map(int, f.readline().split())) for _ in range(m)]

    result = count_connected_components(n, edges)

    with open("output.txt", "w") as f:
        f.write(str(result) + "\n")
