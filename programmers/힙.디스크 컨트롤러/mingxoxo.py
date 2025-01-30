from heapq import heappush, heappop

def solution(jobs):
    req_heap = []
    total = 0
    
    # 요청 시간 기준 힙 초기화
    for i, times in enumerate(jobs):
        heappush(req_heap, (*times, i))
    
    start = 0
    task_heap = []
    while req_heap or task_heap:
        
        # 작업 힙이 비어 있다면 요청 힙에서 하나 가져오기
        if not task_heap:
            req, dur, idx = heappop(req_heap)
            heappush(task_heap, (dur, req, idx))
        
        # 현재 작업 처리
        dur, req, idx = heappop(task_heap)
        start = max(start, req)
        end = start + dur

        total += end - req
        start = end
        
        # 시작 가능 작업을 작업 힙에 추가
        while req_heap and req_heap[0][0] <= start:
            req, dur, idx = heappop(req_heap)
            heappush(task_heap, (dur, req, idx))
    
    return int(total / len(jobs))
