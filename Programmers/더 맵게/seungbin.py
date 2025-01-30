import heapq
def solution(scoville, K):
    cnt=0
    heapq.heapify(scoville) # 최소 힙으로 변환
    
    while(scoville[0]<K):
        if len(scoville)==1: # K를 넘기지 못 할 경우
            return -1
        
        sco_1 = heapq.heappop(scoville) # 가장 맵지 않은 음식
        sco_2 = heapq.heappop(scoville) # 다음으로 맵지 않은 음식
        
        heapq.heappush(scoville, sco_1 + sco_2 * 2) # 새로운 음식 만들어서 추가
        cnt+=1 # 섞은 횟수 업데이트
        
    return cnt
