import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # scoville을 heap 형태로 변환
    while len(scoville) > 1 and scoville[0] < K:
        # 새로운 음식 만들기
        mix = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        # 새롭게 만든 음식의 스코빌 지수 추가
        heapq.heappush(scoville, mix)
        answer += 1 # 횟수 추가
    
    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1 반환
    if scoville[0] < K: 
        return -1
    return answer
