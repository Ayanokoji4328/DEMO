class Graph:
    def __init__(self, matrix):
        self.V = len(matrix)
        self.edges = [(matrix[i][j], i, j)
                      for i in range(self.V)
                      for j in range(i + 1, self.V)
                      if matrix[i][j]]

    def kruskal_mst(self):
        parent = list(range(self.V))
        rank = [0] * self.V

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(x, y):
            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1

        mst = []
        for w, u, v in sorted(self.edges):
            x, y = find(u), find(v)
            if x != y:
                mst.append((u, v, w))
                union(x, y)

        print("Edges in MST:")
        for u, v, w in mst:
            print(f"{u} -- {v} == {w}")
        print("Minimum Cost:", sum(w for _, _, w in mst))


# Predefined adjacency matrix
matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

Graph(matrix).kruskal_mst()
