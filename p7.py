import heapq

def prim_mst(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_heap = [(0, 0, -1)]
    mst_cost = 0
    mst_edges = []

    while len(mst_edges) < num_vertices - 1:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight
        if parent != -1:
            mst_edges.append((parent, u, weight))
        for v in range(num_vertices):
            w = graph[u][v]
            if w > 0 and not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst_cost, mst_edges

# Predefined adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Compute MST
min_cost, min_edges = prim_mst(graph)

# Print result
print("Minimum Cost Spanning Tree (MST) Edges:")
for u, v, w in min_edges:
    print(f"Edge ({u} - {v}) with weight {w}")
print("Total Minimum Cost of MST:", min_cost)
