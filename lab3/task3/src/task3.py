import sys
import time
import tracemalloc

sys.setrecursionlimit(2000)


def has_cycle(v, graph, visited, stack):
    visited[v] = True
    stack[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if has_cycle(neighbor, graph, visited, stack):
                return True
        elif stack[neighbor]:
            return True

    stack[v] = False
    return False


def detect_cycle(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)

    visited = {i: False for i in range(1, n + 1)}
    stack = {i: False for i in range(1, n + 1)}

    for node in range(1, n + 1):
        if not visited[node]:
            if has_cycle(node, graph, visited, stack):
                return 1
    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n, m = map(int, f.readline().split())
        edges = [tuple(map(int, f.readline().split())) for _ in range(m)]

    tracemalloc.start()
    start_time = time.time()

    result = detect_cycle(n, edges)

    end_time = time.time()
    memory_used = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    with open("output.txt", "w") as f:
        f.write(str(result) + "\n")


    print(f"Time: {end_time - start_time:.6f} sec")
    print(f"Memory: {memory_used / 1024:.2f} KB")
