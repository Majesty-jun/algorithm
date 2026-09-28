import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N + 1)

    for _ in range(M):
        index, value = map(int, input().split())
        nodes[index] = value

    for i in range(N, 1, -1):
        nodes[i // 2] += nodes[i]

    print(f'#{test_case} {nodes[L]}')