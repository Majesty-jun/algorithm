import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    answers = list(map(int, input().split()))
    students = [list(map(int, input().split())) for _ in range(N)]

    max_scores = 0
    min_scores = float("INF")
    for i in range(N):
        curr_student_score = 0
        combo_cnt = 0
        for j in range(M):
            if answers[j] == students[i][j]:
                curr_student_score += (combo_cnt + 1)
                combo_cnt += 1
            else:
                combo_cnt = 0

        max_scores = max(max_scores, curr_student_score)
        min_scores = min(min_scores, curr_student_score)

    print(f'#{test_case} {max_scores - min_scores}')
