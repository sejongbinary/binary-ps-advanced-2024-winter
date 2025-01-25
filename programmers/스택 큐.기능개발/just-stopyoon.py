def solution(progresses, speeds):
    answer = [] # 최종 정답
    day = 1 # 작업 일자
    cnt = 0 # 배포하는 기능의 개수
    
    while (len(progresses) != 0) : # 남은 기능이 없을 때까지
        if progresses[0] + speeds[0] * day >= 100 : # 기능이 완성되면
            progresses.pop(0) # 해당 기능 배포
            speeds.pop(0) # 해당 개발속도 없애기
            cnt += 1 # 배포하는 기능의 개수 증가
        else : # 아직 기능이 완성되지 않았다면
            if cnt > 0 : # 지금까지 배포할 수 있는 기능이 있다면
                answer.append(cnt) # 해당 배포에 배포되는 기능 수 추가
                cnt = 0 # 개수 초기화
            day += 1 # 일자 주가
    if cnt > 0 : # 모든 기능 배포가 끝났을 때 마지막으로 배포해야하는 기능들이 있다면
        answer.append(cnt) # 해당 배포에 배포되는 기능 수 추가
    return answer
