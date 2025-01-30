def solution(progresses, speeds):
    answer = []
    release_day = 0
    
    for progress, speed in zip(progresses, speeds):
        # 필요한 작업 일자 계산
        div, mod = divmod(100 - progress, speed)
        processing_day = div + int(mod != 0)

        # 이전 작업과 함께 배포가 가능한 경우
        if processing_day <= release_day:
            answer[-1] += 1
            continue

        # 새 배포일 갱신
        answer.append(1)
        release_day = processing_day
        
    return answer
