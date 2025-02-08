def solution(sizes):
    min_len, max_len = 0, 0
    
    for w, h in sizes:
        min_len = max(min_len, min(w, h))
        max_len = max(max_len, max(w, h))

    return min_len * max_len
