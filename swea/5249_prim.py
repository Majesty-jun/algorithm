import heapq
import sys
sys.stdin = open('input.txt')


def mst_prim(p_vertices, p_edges):
    mst = []
    visited = set()

    adj_v = {x:[] for x in p_vertices}
    for start_node, end_node, weight in p_edges:
        adj_v[start_node].append((end_node, weight))
        adj_v[end_node].append((start_node, weight))

    init_vertex = p_vertices[0]
    min_heap = [[w, init_vertex, e] for e, w in adj_v[init_vertex]]
    heapq.heapify(min_heap)
    visited.add(p_vertices[0])
    


    return mst

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    vertices = [i for i in range(V + 1)]

    for i in range(E):
        edges.append(list(map(int, input().split())))

    mst_prim(vertices, edges)

    print(f'#{test_case} {edges}')
