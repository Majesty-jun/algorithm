import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    V, E, N1, N2 = map(int, input().split())
    tree = list(map(int, input().split()))

    children = [[] for _ in range (V + 1)]
    parent = [0] * (V + 1)

    for i in range(0, len(tree), 2):
        p, c = tree[i], tree[i + 1]
        children[p].append(c)
        parent[c] = p

    ancestors = set()
    x = N1
    while x:
        ancestors.add(x)
        x = parent[x]

    y = N2
    while y not in ancestors:
        y = parent[y]

    common_root = y

    size = 0
    stack = [common_root]
    while stack:
        node = stack.pop()
        size += 1
        stack.extend(children[node])

    print(f'#{test_case} {common_root} {size}')
    
