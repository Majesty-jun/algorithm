import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input.txt')

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def find_goal():
    queue = deque()
    queue.append((1, 1))
    matrix[1][1] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
    
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 1:
                if matrix[nx][ny] == 3:
                    return 1
                
                matrix[nx][ny] = 1
                queue.append((nx, ny))

    return 0

for test_case in range(1, 11): 
    N = 16
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    result = find_goal()


    print(f'#{test_case} {result}')
