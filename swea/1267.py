import sys

sys.stdin = open("sample_input.txt")

from collections import defaultdict

for test_case in range(1, 11):
    V, E = map(int, input().split())
    nodes = list(map(int, input().split()))
    graph = defaultdict(list)
    visited = set()
    result = []
    for i in range(0, len(nodes), 2):
        graph[nodes[i]].append(nodes[i + 1])

    def dfs(v):
        visited.add(v)

        for adj_v in graph[v]:
            if adj_v in visited:
                continue
            dfs(adj_v)

        result.append(v)

    for v in range(1, V + 1):
        if v in visited:
            continue
        dfs(v)

    rev_result = list(map(str, result[::-1]))
    print(f"#{test_case} {' '.join(rev_result)}")
