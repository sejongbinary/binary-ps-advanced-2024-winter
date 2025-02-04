from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville) # 최소힙으로 재배열
    
    while 1 < len(scoville) and scoville[0] < K:
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        answer += 1

    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1
    if scoville[0] < K: 
        return -1
    return answer
