import sys
sys.stdin = open('input.txt', 'r')


def find(x):
    for i in range(len(edges)):
        if x in edges[i]:
            x = i
    return x


def dfs(curr_N1_node, curr_N2_node):
    global common_root

    if curr_N1_node == curr_N2_node:
        common_root = curr_N1_node
        return

    if curr_N1_node > curr_N2_node:
        curr_N1_node = find(curr_N1_node)
    else:
        curr_N2_node = find(curr_N2_node)

    dfs(curr_N1_node, curr_N2_node)


def find_subtree_size(root):
    global size

    if len(edges[root]) == 0:
        return

    for vertex in edges[root]:
        size += 1
        find_subtree_size(vertex)


T = int(input())
for test_case in range(1, T + 1):
    V, E, N1, N2 = map(int, input().split())
    tree = list(map(int, input().split()))
    edges = [[] for _ in range(V + 1)]

    common_root = 0
    size = 1

    for i in range(0, len(tree), 2):
        edges[tree[i]].append(tree[i + 1])

    dfs(N1, N2)
    find_subtree_size(common_root)
    print(f'#{test_case } {common_root} {size}')