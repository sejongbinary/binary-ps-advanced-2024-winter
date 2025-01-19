def solution(progresses, speeds):
    date = [-((p - 100)//s) for p, s in zip(progresses, speeds)] # 각 작업이 며칠 걸리는지 확인
    answer = [] 
    idx = 0
    while idx != len(date): # 모든 일정을 돌 때 까지
        answer.append(1) # 일단 하루 추가 
        cmp = idx + 1 # 비교할 다음날 index
        while cmp != len(date): # 모든 일정을 돌 때 까지 비교 
            if date[idx] >= date[cmp]: #만약 다음 일정이 기준 idx보다 빨리 끝난 경우 
                answer[-1] += 1 
            else:
                break
            cmp += 1 # 계속 비교 
        idx = cmp # 비교한 만큼 증가
 
    return answer