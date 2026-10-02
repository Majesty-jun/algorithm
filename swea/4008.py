import sys
sys.stdin = open('input.txt')


def dfs(acc, depth):
    global max_num, min_num

    if depth == N:
        max_num = max(max_num, acc)
        min_num = min(min_num, acc)
        return

    for op_idx, op_cnt in enumerate(operations):
        if op_cnt == 0: 
            continue

        tmp_acc = acc
        if op_idx == 0:
            tmp_acc += numbers[depth]
        if op_idx == 1:
            tmp_acc -= numbers[depth]
        if op_idx == 2:
            tmp_acc *= numbers[depth]
        if op_idx == 3:
            if numbers[depth] == 0:
                return
            tmp_acc = int(tmp_acc / numbers[depth])

        operations[op_idx] -= 1
        dfs(tmp_acc, depth + 1)
        operations[op_idx] += 1



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    operations = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_num = float('-INF')
    min_num = float('INF')

    dfs(numbers[0], 1)

    print(f'#{test_case} {max_num - min_num}')