import sys
sys.stdin = open('input.txt')

class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)

    def make_set(self, x):
        self.p[x] = x

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px < py:
            self.p[py] = px
        else:
            self.p[px] = py

def mst_kruskal(vertices, edges):
    mst = []
    n = len(vertices)
    ds = DisjointSet(vertices)

    for i in range(n + 1):
        ds.make_set(i)
    
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        s, e, w = edge
        if ds.find_set(s) != ds.find_set(e):
            ds.union(s, e)
            mst.append(edge)

    return mst


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    nodes = []
    vertice = [i for i in range(V + 1)]

    for i in range(E):
        nodes.append(list(map(int, input().split())))


    result = 0
    for s, e, w in mst_kruskal(vertice, nodes):
        result += w

    print(f'#{test_case} {result}')