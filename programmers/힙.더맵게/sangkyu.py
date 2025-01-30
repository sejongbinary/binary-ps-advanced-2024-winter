import heapq

def solution(hot, K):
    cnt = 0
    heapq.heapify(hot) # 스코빌 배열을 힙에 넣기 
    while hot[0] < K: # 가장 작은 스코빌 지수가 K를 넘기전까지
        if len(hot) == 1: # K를 넘게 만들 수 없는 경우 
            return -1
        heapq.heappush(hot, heapq.heappop(hot) + 2 * heapq.heappop(hot)) # 섞기
        cnt += 1
    return cnt
    