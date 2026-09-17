def solution(sizes):
    answer = 0
    
    max_short = 0
    max_long = 0
    for size in sizes:
        sorted_size = sorted(size)
        
        max_short = max(max_short, sorted_size[0])
        max_long = max(max_long, sorted_size[1])
    
    answer = max_short * max_long
    
    return answer