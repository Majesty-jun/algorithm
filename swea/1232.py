from collections import defaultdict
import sys
sys.stdin = open('input.txt')


operations = ['+', '-', '*', '/']


def dfs(curr_node):
    global result
    value = values[curr_node]

    if value not in operations:
        return int(value)

    left = dfs(nodes[curr_node][0])
    right = dfs(nodes[curr_node][1])

    if value in operations:
        if value == '+':
            return left + right
        if value == '-':
            return left - right
        if value == '*':
            return left * right
        if value == '/':
            if value == 0:
                return
            return int(left / right)


for test_case in range(1, 11):
    N = int(input())
    nodes = defaultdict(list)
    values = [''] * (N + 1)

    for i in range(N):
        edge = list(input().split())
        values[int(edge[0])] = edge[1]

        if len(edge) >= 3:
            nodes[int(edge[0])] = (list(map(int, edge[2:])))

    result = dfs(1)

    print(f'#{test_case} {result}')
