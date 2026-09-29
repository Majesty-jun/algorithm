import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')

def dfs(node):
    if len(tree[node]) >= 1:
        dfs(tree[node][0])

    result.append(letters[node])
    
    if len(tree[node]) >= 2:
        dfs(tree[node][1])
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = defaultdict(list)
    letters = [''] * (N + 1)
    result = []

    for i in range(N):
        edge = list(input().split())
        node = int(edge[0])
        tree[node] = list(map(int, edge[2:]))
        letters[node] = edge[1]

    dfs(1)

    print(f'{test_case} {"".join(result)}')