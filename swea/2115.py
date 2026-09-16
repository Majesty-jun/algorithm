import itertools

def get_curr_max(i, j):
    honey_max = 0
    for selected_num in range(1, M + 1):
        comb = itertools.combinations(honey_matrix[i][j:j+M], selected_num)

        for nums in comb:
            if sum(nums) > C:
                continue

            honey_max = max(honey_max, sum(map(lambda x: x**2, nums)))
    return honey_max

T = int(input())
for test_case in range(1, T + 1):
    # 작업자 1에 대한 완전탐색을 진행.
    # 작업자 1에 대한 완전탐색을 진행하는 단계마다
    # 작업자 1의 다음 꿀통부터 시작해서
    # 작업자 2의 완전탐색을 진행.

    # 작업자 1의 완전탐색 내부에서 작업자 2의 완전탐색 진행하며
    # 모든 경우의 수 체크해서 최댓값만 추출하여 total_max에 더함
    N, M, C = map(int, input().split())
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]
    total_max = 0

    for first_i in range(N):
        for first_j in range(N - M + 1):
            first_honey_max = get_curr_max(first_i, first_j)

            for second_i in range(first_i, N):
                for second_j in range(N - M + 1):
                    if second_i == first_i and second_j < first_j + M:
                        continue

                    second_honey_max = get_curr_max(second_i, second_j)
                    
                    total_max = max(total_max, first_honey_max + second_honey_max)

    print(f'#{test_case} {total_max}')
